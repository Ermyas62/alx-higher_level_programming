-- Create database and the user
-- If the user exist, script fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `htbn_0d_2`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES
