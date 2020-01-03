-- Final project creatings tables
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS Person, Location, SocialLife, Degree, Fulfills, MajorTable, MinorTable;
SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE Person (
	id int auto_increment,
    name varchar(64) NOT NULL DEFAULT '',
    email varchar(64) UNIQUE,
    ethnicity varchar(64) NOT NULL DEFAULT '',
    gender varchar(64) NOT NULL DEFAULT '',
    contact varchar(100) NOT NULL DEFAULT '', -- optional
    needContact varchar(64) NOT NULL DEFAULT '', -- optional

	PRIMARY KEY(id)
);


CREATE TABLE SocialLife (
	id int auto_increment,
    personId int, -- FK to Person
    living set('on campus', 'within 5 miles of campus', '5+ miles away from campus'),
    hangout varchar(64) NOT NULL DEFAULT '',
    pals varchar(64) NOT NULL DEFAULT '',
    meetPals varchar(64) NOT NULL DEFAULT '',
    campusHobbies varchar(64), -- optional
    offHobbies varchar(150), -- optional
    
    PRIMARY KEY(id)
);

CREATE TABLE Degree (
	id int auto_increment,
    personId int, -- FK to Person
    majorId int, -- FK to Major 
    minorId int, -- FK to Minor
    yearr set('freshman', 'sophomore', 'junior', 'senior', 'senior+'),
    fourYear set('yes', 'no'),
    job set('yes', 'no'),
    
    PRIMARY KEY(id)
);

CREATE TABLE MajorTable (
	id int auto_increment,
	major varchar(64) NOT NULL UNIQUE DEFAULT '',
    
    PRIMARY KEY(id)
);

CREATE TABLE MinorTable(
	id int auto_increment,
    minor varchar(64) NOT NULL UNIQUE DEFAULT 'No minor', -- optional,
    
	PRIMARY KEY(id)
);

    
ALTER TABLE SocialLife
	ADD FOREIGN KEY (personId) REFERENCES Person (id);
    
ALTER TABLE Degree
	ADD FOREIGN KEY (personId) REFERENCES Person (id),
    ADD FOREIGN KEY (majorId) REFERENCES MajorTable (id),
    ADD FOREIGN KEY (minorId) REFERENCES MinorTable (id);
    


    
    

	