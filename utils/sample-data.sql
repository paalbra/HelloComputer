PRAGMA foreign_keys = ON;

INSERT INTO computer(name, secret) VALUES("HAL9000", "BAY DOORS");
INSERT INTO computer(name, secret, description) VALUES("WOPR", "GLOBAL THERMONUCLEAR WAR", "WAR OPERATION PLAN RESPONSE");

INSERT INTO hello(computer_id, ipaddress) VALUES(1, "127.0.0.1");
INSERT INTO hello(computer_id, ipaddress) VALUES(1, "::1");
INSERT INTO hello(datetime, computer_id, ipaddress) VALUES("1970-01-01 00:00:00", 2, "192.168.0.0");
