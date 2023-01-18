-- migrate:up
INSERT INTO location_types
VALUES (DEFAULT, 'Buffer'),
       (DEFAULT, 'Cell');

INSERT INTO unit_types
VALUES (DEFAULT, 'Box');

-- migrate:down
