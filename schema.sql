DROP TABLE IF EXISTS images;

CREATE TABLE images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imgname TEXT NOT NULL,
    imgurl TEXT NOT NULL,
    imgdetails TEXT NOT NULL
);