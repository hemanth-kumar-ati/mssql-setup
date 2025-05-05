# mssql-python-app

This project is a Python application that connects to a Microsoft SQL Server (MSSQL) database running in a Docker container. It demonstrates how to set up the environment, build the Docker image, and interact with the database using Python.

## Project Structure

```
mssql-python-app
├── src
│   ├── main.py          # Main entry point of the application
│   └── config
│       └── database.py  # Database configuration settings
├── docker
│   ├── Dockerfile       # Instructions for building the MSSQL Docker image
│   └── init.sql         # SQL commands for initializing the database
├── requirements.txt      # Python dependencies
├── docker-compose.yml    # Docker services configuration
├── .env                  # Environment variables for the project
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd mssql-python-app
   ```

2. **Build the Docker image:**
   ```bash
   docker-compose build
   ```

3. **Run the application:**
   ```bash
   docker-compose up
   ```

4. **Access the application:**
   The application will connect to the MSSQL database as specified in the configuration files.

## Usage

- Modify the `.env` file to set your database credentials and connection settings.
- Update `init.sql` to define your database schema or seed initial data.
- Use `src/main.py` to implement your application logic for interacting with the database.

## Dependencies

This project requires the following Python libraries:
- `pyodbc` or `pymssql` for connecting to the MSSQL database.

## License

This project is licensed under the MIT License. See the LICENSE file for details.