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
    id           serial PRIMARY KEY,
    barcode      varchar(40) UNIQUE       NOT NULL,
    unit_barcode varchar(40)              NOT NULL,
    sku_id       int REFERENCES skus (id) NOT NULL,
    supply_id    int
);
-- migrate:down
