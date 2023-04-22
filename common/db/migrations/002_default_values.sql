-- migrate:up
INSERT INTO location_types
VALUES (1, 'Buffer'),
       (2, 'Rack');

INSERT INTO unit_types
VALUES (1, 'Cell'),
       (2, 'Box');

INSERT INTO settings (key, value)
VALUES ('warehouse_size', '{"block_size": 25, "width": 32, "height": 17}'),
       ('distance_calc_status', '0');

-- migrate:down
