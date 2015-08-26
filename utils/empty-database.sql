PRAGMA foreign_keys = ON;

CREATE TABLE hello (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  datetime    TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  computer_id INTEGER NOT NULL,
  ipaddress   TEXT NOT NULL,

  FOREIGN KEY(computer_id) REFERENCES computer(id)
);

CREATE TABLE computer (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  name        TEXT NOT NULL,
  secret      TEXT NOT NULL,
  description TEXT DEFAULT NULL
);
