CREATE TABLE IF NOT EXISTS students(
    id SERIAL PRIMARY KEY,
    nom VARCHAR(50),
    promo VARCHAR(50)
);

INSERT INTO students (nom, promo)
VALUES ('alice', '2024');