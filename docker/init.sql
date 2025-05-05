IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'dbtest')
BEGIN
    CREATE DATABASE dbtest;
END