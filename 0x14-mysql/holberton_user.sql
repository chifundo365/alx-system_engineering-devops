# Creates MySQL user 'holberton user'
# the user has has permission to check the primary/replica status of database

DROP USER IF EXISTS 'holberton_user'@'localhost';
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT, SELECT, INSERT  ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
