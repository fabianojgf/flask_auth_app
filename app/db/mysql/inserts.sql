INSERT INTO general.permission_type (id, description) VALUES
(nextval('general.permission_type_seq'), 'Gerenciador de Usuários'),
(nextval('general.permission_type_seq'), 'Gerenciador de Dados');

INSERT INTO general.permission_status (id, description) VALUES
(nextval('general.permission_status_seq'), 'Solicitado'),
(nextval('general.permission_status_seq'), 'Solicitação Negada'),
(nextval('general.permission_status_seq'), 'Ativo'),
(nextval('general.permission_status_seq'), 'Cancelado');

INSERT INTO general.user_type (id, description) VALUES
(nextval('general.user_type_seq'), 'Admin'),
(nextval('general.user_type_seq'), 'Comum');