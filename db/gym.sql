DROP TABLE bookings;
DROP TABLE members;
DROP TABLE lessons;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    duration INT,
    start_time VARCHAR(255),
    capacity INT
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id),
    lesson_id INT REFERENCES lessons(id)
);