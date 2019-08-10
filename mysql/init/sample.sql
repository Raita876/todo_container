SET CHARSET UTF8;
CREATE DATABASE
IF NOT EXISTS todo_app
DEFAULT CHARACTER
SET utf8;

USE todo_app;

CREATE TABLE todo
(
    id VARCHAR(40),
    name VARCHAR(40),
    tag VARCHAR(30),
    memo VARCHAR(140),
    create_date DATETIME,
    update_date DATETIME,
    close_date DATETIME
);

INSERT INTO todo
    (id, name, tag, memo, create_date, update_date, close_date)
VALUES
    ("378b8717-f821-4fde-bdc0-29b11d88840b", "Sample1", "AAA", "I'm Sample AAA! Hello World!!", "2019-01-01 00:00:00", "2019-02-01 00:00:00", "2019-03-01 00:00:00");

INSERT INTO todo
    (id, name, tag, memo, create_date, update_date, close_date)
VALUES
    ("45d675f5-688c-4c84-a5de-9aec78e4d017", "Sample2", "BBB", "HAHAHA! Nice to meet you!", "2019-11-11 12:12:00", "2019-05-05 12:05:00", "2019-05-25 23:00:00");

INSERT INTO todo
    (id, name, tag, memo, create_date, update_date, close_date)
VALUES
    ("2e3d6127-4a92-4ff5-a6dc-f995a24850b6", "Sample3", "CCC", "How are you? This is a pen.", "2019-01-01 00:00:00", "2019-01-01 00:00:00", "2019-01-01 00:00:00");
