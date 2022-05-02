DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS gym_classes;
DROP TABLE IF EXISTS class_types;
DROP TABLE IF EXISTS start_times;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS membership_types;


CREATE TABLE membership_types (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255)
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    membership_number INT,
    membership_type_id INT references membership_types(id),
    active_status BOOLEAN
);

CREATE TABLE class_types (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    intensity INT,
    description VARCHAR(255)
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE start_times (
    id SERIAL PRIMARY KEY,
    time VARCHAR(255)
);

CREATE TABLE gym_classes (
    id SERIAL PRIMARY KEY,
    class_type_id INT REFERENCES class_types(id),
    start_time_id INT REFERENCES start_times(id),
    duration INT,
    location_id INT REFERENCES locations(id),
    capacity INT
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    gym_class_id INT REFERENCES gym_classes(id) ON DELETE CASCADE
);