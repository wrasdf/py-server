CREATE ROLE postgresql superuser;
CREATE DATABASE pyserver OWNER postgresql;
CREATE TABLE IF NOT EXISTS users (
  id serial PRIMARY KEY,
  logdate timestamp,
  user_name text not null unique,
  email text not null unique,
  password text not null
);
