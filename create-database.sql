CREATE DATABASE coincollector;

CREATE USER coin_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE coincollector TO coin_admin;