env
sleep 20
/opt/mssql-tools18/bin/sqlcmd -C -S db1 -U sa -P Qwerty123! -i /mnt/backup/db1/create_tables.sql
/opt/mssql-tools18/bin/sqlcmd -C -S db1 -U sa -P Qwerty123! -i /mnt/backup/db1/insert_data.sql
/opt/mssql-tools18/bin/sqlcmd -C -S db2 -U sa -P Qwerty123! -i /mnt/backup/db2/create_tables.sql
/opt/mssql-tools18/bin/sqlcmd -C -S db2 -U sa -P Qwerty123! -i /mnt/backup/db2/insert_data.sql
sleep infinity