-- creates the table id_not_null on the server
-- description of id_not_null
--    id INT with default value 1
--    name VARCHAR(256)
-- the database will be passed as an arguement of the mysql command
-- if the table already exists, script should not fail

CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256)
);
