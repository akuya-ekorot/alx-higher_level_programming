-- creates the table unique_id
-- unique_id description
--    id INT DEFAULT 1 UNIQUE,
--    name VARCHAR(256)
-- database name will be passed as an argument
-- if table already exists script should not fail

CREATE TABLE IF NOT EXISTS unique_id(
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
