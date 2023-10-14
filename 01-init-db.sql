-- CREATE TABLE
DROP TABLE IF EXISTS question;
CREATE TABLE question (
    id SERIAL PRIMARY KEY,
    text TEXT,
    answer TEXT,
    creation_date DATE
);
