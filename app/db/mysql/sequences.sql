-- DROP SEQUENCE general.access_seq;

CREATE SEQUENCE general.access_seq
    INCREMENT BY 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1
    NO CYCLE;

-- Permissions

ALTER SEQUENCE general.access_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE general.access_seq TO postgres;
GRANT SELECT ON SEQUENCE general.access_seq TO postgres;

-- DROP SEQUENCE general.department_seq;

CREATE SEQUENCE general.department_seq
    INCREMENT BY 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1
    NO CYCLE;

-- Permissions

ALTER SEQUENCE general.department_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE general.department_seq TO postgres;
GRANT SELECT ON SEQUENCE general.department_seq TO postgres;

-- DROP SEQUENCE general.permission_seq;

CREATE SEQUENCE general.permission_seq
    INCREMENT BY 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1
    NO CYCLE;

-- Permissions

ALTER SEQUENCE general.permission_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE general.permission_seq TO postgres;
GRANT SELECT ON SEQUENCE general.permission_seq TO postgres;

-- DROP SEQUENCE general.permission_type_seq;

CREATE SEQUENCE general.permission_type_seq
    INCREMENT BY 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1
    NO CYCLE;

-- Permissions

ALTER SEQUENCE general.permission_type_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE general.permission_type_seq TO postgres;
GRANT SELECT ON SEQUENCE general.permission_type_seq TO postgres;

-- DROP SEQUENCE general.permission_status_seq;

CREATE SEQUENCE general.permission_status_seq
    INCREMENT BY 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1
    NO CYCLE;

-- Permissions

ALTER SEQUENCE general.permission_status_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE general.permission_status_seq TO postgres;
GRANT SELECT ON SEQUENCE general.permission_status_seq TO postgres;

-- DROP SEQUENCE general.user_type_seq;

CREATE SEQUENCE general.user_type_seq
    INCREMENT BY 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1
    NO CYCLE;

-- Permissions

ALTER SEQUENCE general.user_type_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE general.user_type_seq TO postgres;
GRANT SELECT ON SEQUENCE general.user_type_seq TO postgres;

-- DROP SEQUENCE general.user_seq;

CREATE SEQUENCE general.user_seq
    INCREMENT BY 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    START 1
    CACHE 1
    NO CYCLE;

-- Permissions

ALTER SEQUENCE general.user_seq OWNER TO postgres;
GRANT ALL ON SEQUENCE general.user_seq TO postgres;
GRANT SELECT ON SEQUENCE general.user_seq TO postgres;

--DROP TABLE general.access_seq;
--DROP TABLE general.permission_seq;
--DROP TABLE general.permission_type_seq;
--DROP TABLE general.permission_status_seq;
--DROP TABLE general.department_seq;
--DROP TABLE general.user_seq;

---------------------------------------------------------------------------------