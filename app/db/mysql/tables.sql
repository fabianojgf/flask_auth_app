-- Database: chat-data

-- DROP DATABASE IF EXISTS "chat-data";

CREATE DATABASE "chat-data"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Portuguese_Brazil.1252'
    LC_CTYPE = 'Portuguese_Brazil.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
-- SCHEMA: general

-- DROP SCHEMA IF EXISTS general ;

CREATE SCHEMA IF NOT EXISTS general
    AUTHORIZATION postgres;

---------------------------------------------------------------------------------
	
BEGIN;

CREATE TABLE IF NOT EXISTS general.department
(
    id int4 NOT NULL,
    name character varying(200) NOT NULL,
	sigla character varying(10) NOT NULL,
    parent_id int4 NULL,
    active boolean DEFAULT true,
    creation_date timestamp without time zone,
    update_date timestamp without time zone,
    
	CONSTRAINT department_pkey 
		PRIMARY KEY (id),
    CONSTRAINT parent_id_fkey 
		FOREIGN KEY (parent_id)
		REFERENCES general.department (id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
		NOT VALID
)
WITH (
    OIDS = FALSE
);

CREATE TABLE IF NOT EXISTS general.permission_type
(
    id int4 NOT NULL,
    description character varying(30) NOT NULL,
    
	CONSTRAINT permission_type_pkey 
		PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE IF NOT EXISTS general.permission_status
(
    id int4 NOT NULL,
    description character varying(30) NOT NULL,
    
	CONSTRAINT permission_status_pkey 
		PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE IF NOT EXISTS general.user_type
(
    id int4 NOT NULL,
    description character varying(30) NOT NULL,
    
	CONSTRAINT user_type_pkey 
		PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
);

CREATE TABLE IF NOT EXISTS general."user"
(
    id int4 NOT NULL,
    name character varying(200) NOT NULL,
    email character varying(200) NOT NULL,
    password character varying(200) NOT NULL,
    user_type_id int4 NOT NULL,
    active boolean DEFAULT true,
    authorized boolean DEFAULT false,
    creation_date timestamp without time zone,
    update_date timestamp without time zone,
    
	CONSTRAINT user_pkey 
		PRIMARY KEY (id),
	CONSTRAINT user_type_id_fkey 
		FOREIGN KEY (user_type_id)
		REFERENCES general.user_type (id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
		NOT VALID
)
WITH (
    OIDS = FALSE
);

COMMENT ON COLUMN general."user".type is 'User type: 1 - ADMIN; 2 - COMMON';

CREATE TABLE IF NOT EXISTS general.permission
(
    id int4 NOT NULL,
    user_id int4 NOT NULL,
    department_id int4,
    permission_type_id int4 NOT NULL,
    permission_status_id int4 NOT NULL,
    begin date,
    "end" date,
    active boolean DEFAULT true,
    creation_date timestamp without time zone,
    update_date timestamp without time zone,
    
	CONSTRAINT permission_pkey 
		PRIMARY KEY (id),
	CONSTRAINT department_id_fkey 
		FOREIGN KEY (department_id)
		REFERENCES general.department (id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
		NOT VALID,
	CONSTRAINT permission_type_id_fkey 
		FOREIGN KEY (permission_type_id)
		REFERENCES general.permission_type (id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
		NOT VALID,
	CONSTRAINT permission_status_id_fkey 
		FOREIGN KEY (permission_status_id)
		REFERENCES general.permission_status (id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
		NOT VALID,
	CONSTRAINT user_id_fkey 
		FOREIGN KEY (user_id)
		REFERENCES general."user" (id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
		NOT VALID
)
WITH (
    OIDS = FALSE
);

CREATE TABLE IF NOT EXISTS general.access
(
    id int4 NOT NULL,
    user_id int4 NOT NULL,
    address character varying(30) NULL,
    user_agent text NULL,
    date_in timestamp without time zone NOT NULL,
    date_out timestamp without time zone,
    
	CONSTRAINT access_pkey 
		PRIMARY KEY (id),
	CONSTRAINT user_id_fkey 
		FOREIGN KEY (user_id)
		REFERENCES general."user" (id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
		NOT VALID
)
WITH (
    OIDS = FALSE
);

END;

--DROP TABLE general.access;
--DROP TABLE general.permission;
--DROP TABLE general.permission_type;
--DROP TABLE general.permission_status;
--DROP TABLE general.department;
--DROP TABLE general.user;

---------------------------------------------------------------------------------