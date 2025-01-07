# Database Difference Checker

## Overview
This project helps to identify and generate SQL scripts for the differences between two databases. It can be run manually or inside a container. If you opt to go with containers, you may choose to use the manual `docker compose` or inside DevContainer.

## Prerequisites
- Docker
- Docker Compose
- Visual Studio Code with Remote - Containers extension

## Setup
1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Open in Visual Studio Code**:
    - Open the repository in Visual Studio Code.
    - When prompted, reopen the folder in a DevContainer.

## Running the Project
1. **Start the containers**:
    ```sh
    docker-compose up
    ```

2. **Run the difference checker**:
    ```sh
    python3 db_diff.py
    ```

3. **Check the results**:
    - The generated SQL files will be located in the **generated** directory.
    - If the directory is not empty, the new results will be appended to the existing files (named after a corresponding table).
    - Ensure the directory is empty before running the script to avoid appending by running:
      ```sh
      rm generated/*
      ```

## Additional Data
- For more data, check the SQL scripts inside [create_tables.sql](http://_vscodecontentref_/1) and `./data/backup/db*/insert_data.sql`.
- The scripts have been tested with containerized SQL Server 2022.

## Notes
- It is recommended to test this inside a DevContainer.