-- migrate:up
CREATE TABLE IF NOT EXISTS settings
(
    id    serial PRIMARY KEY,
    key   text NOT NULL,
    value jsonb NOT NULL
);

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
    barcode  varchar(40)                         NOT NULL,
    type_id  int REFERENCES location_types (id)  NOT NULL,
    group_id int REFERENCES location_groups (id) NOT NULL,
    x        int                                 NOT NULL,
    y        int                                 NOT NULL,
    orientation int                              NOT NULL
);

CREATE TABLE IF NOT EXISTS unit_types
(
    id   serial PRIMARY KEY,
    name text NOT NULL
);

CREATE TABLE IF NOT EXISTS units
(
    id                  serial PRIMARY KEY,
    barcode             varchar(40)                    NOT NULL,
    type_id             int REFERENCES unit_types (id) NOT NULL,
    current_location_id int REFERENCES locations (id),
    target_location_id  int REFERENCES locations (id)
);
-- migrate:down
