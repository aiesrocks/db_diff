import json
import os
from sqlalchemy import create_engine
import pandas as pd

def get_engine(config):
    dialect = config['dialect']
    driver = config.get('driver', '')
    username = config['username']
    password = config['password']
    host = config['host']
    port = config['port']
    database = config['database']
    trust_cert = config.get('trust_cert', 'yes')  # Default to 'yes' to trust self-signed certificates
    if driver:
        return create_engine(f"{dialect}+pyodbc://{username}:{password}@{host}:{port}/{database}?driver={driver}&TrustServerCertificate={trust_cert}")
    else:
        return create_engine(f"{dialect}://{username}:{password}@{host}:{port}/{database}")

def get_data(engine, table_name):
    query = f"SELECT * FROM {table_name}"
    return pd.read_sql(query, engine)

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def generate_insert_statements(table_name, df):
    insert_statements = []
    for _, row in df.iterrows():
        columns = ', '.join(row.index)
        values = ', '.join([f"'{str(value).replace("'", "''")}'" for value in row.values])
        insert_statements.append(f"INSERT INTO {table_name} ({columns}) VALUES ({values});")
    return insert_statements

def generate_delete_statements(table_name, df):
    delete_statements = []
    for _, row in df.iterrows():
        conditions = ' AND '.join([f"{col} = '{str(value).replace("'", "''")}'" for col, value in row.items()])
        delete_statements.append(f"DELETE FROM {table_name} WHERE {conditions};")
    return delete_statements

def main():
    try:
        with open('config.json') as f:
            config = json.load(f)
    except FileNotFoundError:
        print("config.json file not found.")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"Error decoding config.json: {e}")
        exit(1)

    try:
        engine1 = get_engine(config['db1'])
        engine2 = get_engine(config['db2'])
    except KeyError as e:
        print(f"Missing configuration key: {e}")
        exit(1)

    tables = config.get('tables', [])
    if not tables:
        print("No tables specified in config.json.")
        exit(1)

    ensure_directory_exists('generated')

    file_counter = 0

    for table in tables:
        try:
            data1 = get_data(engine1, table)
            data2 = get_data(engine2, table)
        except Exception as e:
            print(f"Error fetching data for table {table}: {e}")
            continue
        
        data_diff = []

        # Find rows that exist only in db2
        diff_insert = data2.merge(data1, how='left', indicator=True)
        diff_insert = diff_insert[diff_insert['_merge'] == 'left_only'].drop(columns=['_merge'])
        if not diff_insert.empty:
            data_diff.append((table, 'insert', diff_insert))
        
        # Find rows that exist only in db1
        diff_delete = data1.merge(data2, how='left', indicator=True)
        diff_delete = diff_delete[diff_delete['_merge'] == 'left_only'].drop(columns=['_merge'])
        if not diff_delete.empty:
            data_diff.append((table, 'delete', diff_delete))

        file_counter += 1
        file_name = f'generated/{file_counter:04d}_{table}.sql'
        try:
            with open(file_name, 'w') as f:
                f.write(f"-- Differences in table {table}\n")
                for action, diff in [(action, diff) for t, action, diff in data_diff if t == table]:
                    if action == 'delete':
                        delete_statements = generate_delete_statements(table, diff)
                        for statement in delete_statements:
                            f.write(statement + "\n")
                f.write("\n")
                for action, diff in [(action, diff) for t, action, diff in data_diff if t == table]:
                    if action == 'insert':
                        insert_statements = generate_insert_statements(table, diff)
                        for statement in insert_statements:
                            f.write(statement + "\n")
                f.write("\n")
        except Exception as e:
            print(f"Error writing to file {file_name}: {e}")

if __name__ == "__main__":
    main()
