-- creates database hbtn_0d_2
-- if db already exists script should not fail
-- creates user user_0d_2
-- if user already exists script should not fail
-- user's password should be user_0d_2_pwd

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
