-- migrate:up
CREATE TABLE IF NOT EXISTS location_types
(
    id   serial PRIMARY KEY,
    name text NOT NULL
);

CREATE TABLE IF NOT EXISTS location_groups
(
    id   serial PRIMARY KEY,
    name text NOT NULL
);

CREATE TABLE IF NOT EXISTS locations
(
    id       serial PRIMARY KEY,
    barcode  varchar(40)                        NOT NULL,
    type     int REFERENCES location_types (id)  NOT NULL,
    group_id int REFERENCES location_groups (id) NOT NULL
);

CREATE TABLE IF NOT EXISTS unit_types
(
    id   serial PRIMARY KEY,
    name text NOT NULL
);

CREATE TABLE IF NOT EXISTS units
(
    id               serial PRIMARY KEY,
    type             int REFERENCES unit_types (id) NOT NULL,
    barcode          varchar(40)                   NOT NULL,
    current_location int REFERENCES locations (id) NOT NULL,
    target_location  int REFERENCES locations (id) NOT NULL
);
-- migrate:down
