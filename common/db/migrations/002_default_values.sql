-- migrate:up
INSERT INTO location_types
VALUES (1, 'Buffer'),
       (2, 'Rack');

INSERT INTO unit_types
VALUES (1, 'Cell'),
       (2, 'Box');

-- migrate:down
