-- migrate:up
CREATE TABLE IF NOT EXISTS tasks
(
    id   serial PRIMARY KEY,
    status int NOT NULL
);

CREATE TABLE IF NOT EXISTS needed_skus
(
    id   serial PRIMARY KEY,
    task_id int REFERENCES tasks (id) NOT NULL,
    sku_id int NOT NULL,
    count int NOT NULL
);

CREATE TABLE IF NOT EXISTS picked_products
(
    id   serial PRIMARY KEY,
    task_id int REFERENCES tasks (id) NOT NULL,
    product_barcode varchar(40) NOT NULL,
    sku_id int NOT NULL
);
-- migrate:down
