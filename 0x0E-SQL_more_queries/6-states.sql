-- creates the db hbtn_0d_usa
-- creates table states in the db
-- states description
--    id INT UNIQUE NOT NULL PRIMARY KEY (autogenerated),
--    name VARCHAR(256) NOT NULL

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
