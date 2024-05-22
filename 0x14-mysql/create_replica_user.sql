# Creates a mysql user used for replication named 'replica_user'
# Grants the user the appropriate permissions
# Grants mysql user 'holberton_user' SELECT previlege on the mysql.user table
CREATE USER 'replica_user'@'%';
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
