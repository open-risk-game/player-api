CREATE TABLE players (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(20),
    PRIMARY KEY (id)
);

CREATE TABLE regions (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE territories (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    tokens INT,
    owner INT,
    region_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (owner) REFERENCES players (id),
    FOREIGN KEY (region_id) REFERENCES regions(id)
);

CREATE TABLE boarders (
    id INT NOT NULL AUTO_INCREMENT,
    territory_from_id INT NOT NULL,
    territory_to_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (territory_from_id) REFERENCES territories (id),
    FOREIGN KEY (territory_to_id) REFERENCES territories (id)
);