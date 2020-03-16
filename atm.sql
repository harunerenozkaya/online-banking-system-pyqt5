-- Database: atm

-- DROP DATABASE atm;

CREATE DATABASE atm
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'English_United States.1252'
       LC_CTYPE = 'English_United States.1252'
       CONNECTION LIMIT = -1;



-- Table: public.users

-- DROP TABLE public.users;

CREATE TABLE public.users
(
  id character varying(30) NOT NULL,
  name character varying(30),
  surname character varying(20),
  age integer,
  citizenship_number character varying(30),
  birthdate date,
  balance double precision DEFAULT 0,
  loan double precision DEFAULT 0,
  password character varying(20),
  CONSTRAINT users_pkey PRIMARY KEY (id),
  CONSTRAINT users_citizenship_number_key UNIQUE (citizenship_number)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.users
  OWNER TO postgres;

