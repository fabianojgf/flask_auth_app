GRANT ALL PRIVILEGES ON DATABASE "chat-data" TO "chat-app";

GRANT ALL PRIVILEGES ON SCHEMA "general" TO "chat-app";

GRANT ALL ON TABLE general.user TO "chat-app";
GRANT ALL ON TABLE general.department TO "chat-app";
GRANT ALL ON TABLE general.permission_type TO "chat-app";
GRANT ALL ON TABLE general.permission_status TO "chat-app";
GRANT ALL ON TABLE general.permission TO "chat-app";
GRANT ALL ON TABLE general.access TO "chat-app";

GRANT ALL ON SEQUENCE general.user_seq TO "chat-app";
GRANT ALL ON SEQUENCE general.department_seq TO "chat-app";
GRANT ALL ON SEQUENCE general.permission_type_seq TO "chat-app";
GRANT ALL ON SEQUENCE general.permission_status_seq TO "chat-app";
GRANT ALL ON SEQUENCE general.permission_seq TO "chat-app";
GRANT ALL ON SEQUENCE general.access_seq TO "chat-app";