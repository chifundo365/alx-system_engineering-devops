# Creates a Database called 'tyrell_corp' and a tables called 'nexus6' within the database
# Grants SELECT privilege on the 'tyrell_corp' database to the user 'holbeton_user'@'lcalhost'

CREATE DATABASE tyrell_corp;
CREATE TABLE nexus6(id INT NOT NULL PRIMARY KEY, name VARCHAR(200));
GRANT SELECT ON nexus6.* TO 'holberton_user'@'localhost';
