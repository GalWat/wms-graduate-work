-- migrate:up
CREATE TABLE IF NOT EXISTS tags
(
    id   serial PRIMARY KEY,
    name varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS skus
(
    id      serial PRIMARY KEY,
    name    text NOT NULL,
    tag_ids int[]
);

CREATE TABLE IF NOT EXISTS products
(
    id               serial PRIMARY KEY,
    barcode          varchar(40) UNIQUE NOT NULL,
    location_barcode varchar(40),
    unit_barcode     varchar(40),
    supply_id        int,
    sku_id          int REFERENCES skus (id)
);
-- migrate:down
