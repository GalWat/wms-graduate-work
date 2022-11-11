-- migrate:up
INSERT INTO location_types
VALUES (DEFAULT, 'Buffer'),
       (DEFAULT, 'Cell');

INSERT INTO unit_types
VALUES (DEFAULT, 'Boxing');

-- migrate:down
