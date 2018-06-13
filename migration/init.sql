ALTER USER postgres WITH SUPERUSER;
CREATE DATABASE pyserver OWNER postgres;
CREATE TABLE IF NOT EXISTS users (
  id serial PRIMARY KEY,
  logdate timestamp,
  user_name text not null unique,
  email text not null unique,
  password text not null
);
