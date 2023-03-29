-- creates the table unique_id
-- description of table data: id INT with the default value 1, must be unique & name VARCHAR(256)
-- script  should not fail if data exists

CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
