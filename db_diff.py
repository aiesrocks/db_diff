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

def generate_delete_statements(table_name, df):
    delete_statements = []
    for _, row in df.iterrows():
        delete_statement = f"DELETE FROM {table_name} WHERE id = {row['id']};"  # Assuming 'id' is the primary key
        delete_statements.append(delete_statement)
    return delete_statements

def generate_insert_statements(table_name, df):
    insert_statements = []
    for _, row in df.iterrows():
        columns = ', '.join(row.index)
        values = ', '.join([f"'{str(value).replace("'", "''")}'" for value in row.values])
        insert_statements.append(f"INSERT INTO {table_name} ({columns}) VALUES ({values});")
    return insert_statements

def main():
    try:
        with open('config.json') as f:
            config = json.load(f)
    except FileNotFoundError:
        print("config.json file not found.")
        exit(1)

    engine1 = get_engine(config['db1'])
    engine2 = get_engine(config['db2'])

    tables = config['tables']

    ensure_directory_exists('generated')

    file_counter = 0

    for table in tables:
        data1 = get_data(engine1, table)
        data2 = get_data(engine2, table)
        
        data_diff = []

        # Find rows that exist only in db2
        diff_insert = data2.merge(data1, how='left', indicator=True)
        diff_insert = diff_insert[diff_insert['_merge'] == 'left_only'].drop(columns=['_merge'])
        if not diff_insert.empty:
            data_diff.append(('insert', diff_insert))
        
        # Find rows that exist only in db1
        diff_delete = data1.merge(data2, how='left', indicator=True)
        diff_delete = diff_delete[diff_delete['_merge'] == 'left_only'].drop(columns=['_merge'])
        if not diff_delete.empty:
            data_diff.append(('delete', diff_delete))

        file_counter += 1
        file_name = f'generated/{file_counter:04d}_{table}_diff.sql'
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

        # Clear data_diff for the next table
        data_diff.clear()

if __name__ == "__main__":
    main()
