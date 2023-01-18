CREATE TABLE user (
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	password TEXT NOT NULL,
    create_date TEXT NOT NULL,
    update_date TEXT NULL
);

--DROP TABLE IF EXISTS user;