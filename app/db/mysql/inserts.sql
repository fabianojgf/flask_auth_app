INSERT INTO general.permission_type (id, description) VALUES
(nextval('general.permission_type_seq'), 'User Manager'),
(nextval('general.permission_type_seq'), 'Data Manager');

INSERT INTO general.permission_status (id, description) VALUES
(nextval('general.permission_status_seq'), 'Requested'),
(nextval('general.permission_status_seq'), 'Request denied'),
(nextval('general.permission_status_seq'), 'Active'),
(nextval('general.permission_status_seq'), 'Canceled');