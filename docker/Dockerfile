# Use the official Microsoft SQL Server image
FROM mcr.microsoft.com/mssql/server:2022-latest

USER root
# Install SQL Server tools
RUN apt-get update && apt-get install -y curl gnupg2 && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y mssql-tools unixodbc-dev && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/opt/mssql-tools/bin:${PATH}"

# Set environment variables for SQL Server
ENV ACCEPT_EULA=Y
ENV SA_PASSWORD=YourStrong!Passw0rd
ENV MSSQL_PID=Developer

# Expose the SQL Server port
EXPOSE 1433

# Copy the initialization SQL script
COPY init.sql /usr/src/app/init.sql

# Start SQL Server and run the initialization script
CMD /opt/mssql/bin/sqlservr & \
    sleep 30 && \
    /opt/mssql-tools/bin/sqlcmd \
    -S localhost \
    -U SA \
    -P YourStrong!Passw0rd \
    -i /usr/src/app/init.sql