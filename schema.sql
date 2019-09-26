CREATE TABLE IF NOT EXISTS phone_book (
        id INTEGER PRIMARY KEY,
        surname TEXT NOT NULL,
        firstname TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        address TEXT
    );

INSERT INTO phone_book (surname, firstname, phone_number, address)
VALUES(
'Ritchie',
'Dennis',
"1235813213455",
'19-41 C block'
);

INSERT INTO phone_book (surname, firstname, phone_number, address)
VALUES(
'Stroustrup',
'Bjarne',
"3581321345589",
'19-79 C block'
);

INSERT INTO phone_book (surname, firstname, phone_number, address)
VALUES(
'Noam',
'Chomsky',
"3581321345589",
'19-56 R block'
);

INSERT INTO phone_book (surname, firstname, phone_number, address)
VALUES(
'Dijkstra',
'Edsger',
"3581321345589",
'19-68 Algo'
);