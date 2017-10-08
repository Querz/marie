create database if not exists hackathon;

use hackathon;

create table if not exists cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location_lat DOUBLE,
    location_lng DOUBLE,
    buildings TEXT
);

create table if not exists steps (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(100),
    location_lat DOUBLE,
    location_lng DOUBLE,
    description TEXT
);

create table if not exists step_dependencies (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    step INT,
    dependency INT
);

create table if not exists step_children (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    step INT,
    child INT
);

create table if not exists step_tags (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    step INT,
    tag INT(8)
);

create table if not exists profile (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100),
    language INT(8),
    age INT,
    state_of_family INT(8),
    children INT,
    new_residence VARCHAR(100),
    new_residence_lower VARCHAR(100),
    state_of_work INT(8),
    religion INT(8),
    nationality CHAR(2),
    move_date DATE
);

create table if not exists move_reasons (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    profile INT,
    reason INT(8)
);

create table if not exists profile_steps (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    step INT,
    profile INT,
    time_frame_start DATE,
    time_frame_end DATE,
    status INT(8)
);

insert into cities (name, location_lat, location_lng)
values ("Offenburg", 48.46943049999999, 7.9427725);