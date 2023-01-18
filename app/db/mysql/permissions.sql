GRANT ALL PRIVILEGES ON DATABASE "chat-data" TO "chat-app";

GRANT ALL PRIVILEGES ON SCHEMA "general" TO "chat-app";

GRANT ALL ON TABLE general.user TO "chat-app";

GRANT ALL ON SEQUENCE general.user_seq TO "chat-app";