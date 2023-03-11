-- Generated by Oracle SQL Developer Data Modeler 22.2.0.165.1149
--   at:        2023-03-11 12:29:07 CST
--   site:      Oracle Database 12c
--   type:      Oracle Database 12c



DROP TABLE customer_reviews CASCADE CONSTRAINTS;

DROP TABLE developer CASCADE CONSTRAINTS;

DROP TABLE game CASCADE CONSTRAINTS;

DROP TABLE genre CASCADE CONSTRAINTS;

DROP TABLE language CASCADE CONSTRAINTS;

DROP TABLE platform CASCADE CONSTRAINTS;

DROP TABLE publisher CASCADE CONSTRAINTS;

DROP TABLE relation_10 CASCADE CONSTRAINTS;

DROP TABLE relation_12 CASCADE CONSTRAINTS;

DROP TABLE relation_16 CASCADE CONSTRAINTS;

DROP TABLE user_info CASCADE CONSTRAINTS;

-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE customer_reviews (
    cust_reviews_id         NUMBER NOT NULL,
    cust_reviews_comments   VARCHAR2(2000),
    customer_reviews_is_rec NUMBER,
    cust_reviews_flag       VARCHAR2(100),
    user_id                 NUMBER NOT NULL,
    game_id                 NUMBER NOT NULL
);

ALTER TABLE customer_reviews ADD CONSTRAINT customer_reviews_pk PRIMARY KEY ( cust_reviews_id );

CREATE TABLE developer (
    developer_id          NUMBER,
    developer_name        VARCHAR2(1000),
    developer_image       BLOB,
    developer_country     VARCHAR2(500),
    developer_description VARCHAR2(1000),
    developer_id1         NUMBER NOT NULL
);

ALTER TABLE developer ADD CONSTRAINT developer_pk PRIMARY KEY ( developer_id1 );

CREATE TABLE game (
    game_id                 NUMBER NOT NULL,
    game_name               VARCHAR2(25),
    game_image              BLOB,
    game_despcription       VARCHAR2(2000),
    game_release_date       DATE,
    esrb_rating             VARCHAR2(250),
    publisher_id            NUMBER NOT NULL,
    developer_developer_id1 NUMBER NOT NULL
);

ALTER TABLE game ADD CONSTRAINT game_pk PRIMARY KEY ( game_id );

CREATE TABLE genre (
    genre_id          NUMBER NOT NULL,
    genre_name        VARCHAR2(25),
    genre_description VARCHAR2(500)
);

ALTER TABLE genre ADD CONSTRAINT genre_pk PRIMARY KEY ( genre_id );

CREATE TABLE language (
    lang_id      NUMBER NOT NULL,
    lang_name    VARCHAR2(100),
    lang_charset VARCHAR2(100)
);

ALTER TABLE language ADD CONSTRAINT language_pk PRIMARY KEY ( lang_id );

CREATE TABLE platform (
    platform_id          NUMBER NOT NULL,
    platform_name        VARCHAR2(25),
    platform_image       BLOB,
    platform_description VARCHAR2(1000)
);

ALTER TABLE platform ADD CONSTRAINT platform_pk PRIMARY KEY ( platform_id );

CREATE TABLE publisher (
    publisher_id          NUMBER NOT NULL,
    publisher_name        VARCHAR2(1000),
    publisher_image       BLOB,
    publisher_country     VARCHAR2(500),
    publisher_description VARCHAR2(1000)
);

ALTER TABLE publisher ADD CONSTRAINT publisher_pk PRIMARY KEY ( publisher_id );

CREATE TABLE relation_10 (
    language_lang_id NUMBER NOT NULL,
    game_game_id     NUMBER NOT NULL
);

ALTER TABLE relation_10 ADD CONSTRAINT relation_10_pk PRIMARY KEY ( language_lang_id,
                                                                    game_game_id );

CREATE TABLE relation_12 (
    genre_genre_id NUMBER NOT NULL,
    game_game_id   NUMBER NOT NULL
);

ALTER TABLE relation_12 ADD CONSTRAINT relation_12_pk PRIMARY KEY ( genre_genre_id,
                                                                    game_game_id );

CREATE TABLE relation_16 (
    platform_platform_id NUMBER NOT NULL,
    game_game_id         NUMBER NOT NULL
);

ALTER TABLE relation_16 ADD CONSTRAINT relation_16_pk PRIMARY KEY ( platform_platform_id,
                                                                    game_game_id );

CREATE TABLE user_info (
    user_is_site_admin   NUMBER NOT NULL,
    user_id              NUMBER NOT NULL,
    user_image           BLOB,
    user_fname           VARCHAR2(250),
    user_lname           VARCHAR2(250),
    user_username        VARCHAR2(250),
    user_email           VARCHAR2(250),
    user_password        VARCHAR2(50),
    user_is_on_probation NUMBER,
    user_is_banned       NUMBER,
    user_moderation_mess VARCHAR2(1000)
);

ALTER TABLE user_info ADD CONSTRAINT user_info_pk PRIMARY KEY ( user_id );

ALTER TABLE customer_reviews
    ADD CONSTRAINT customer_reviews_game_fk FOREIGN KEY ( game_id )
        REFERENCES game ( game_id )
            ON DELETE CASCADE;

ALTER TABLE customer_reviews
    ADD CONSTRAINT customer_reviews_user_info_fk FOREIGN KEY ( user_id )
        REFERENCES user_info ( user_id )
            ON DELETE CASCADE;

ALTER TABLE game
    ADD CONSTRAINT game_developer_fk FOREIGN KEY ( developer_developer_id1 )
        REFERENCES developer ( developer_id1 )
            ON DELETE CASCADE;

ALTER TABLE game
    ADD CONSTRAINT game_publisher_fk FOREIGN KEY ( publisher_id )
        REFERENCES publisher ( publisher_id )
            ON DELETE CASCADE;

ALTER TABLE relation_10
    ADD CONSTRAINT relation_10_game_fk FOREIGN KEY ( game_game_id )
        REFERENCES game ( game_id )
            ON DELETE CASCADE;

ALTER TABLE relation_10
    ADD CONSTRAINT relation_10_language_fk FOREIGN KEY ( language_lang_id )
        REFERENCES language ( lang_id )
            ON DELETE CASCADE;

ALTER TABLE relation_12
    ADD CONSTRAINT relation_12_game_fk FOREIGN KEY ( game_game_id )
        REFERENCES game ( game_id )
            ON DELETE CASCADE;

ALTER TABLE relation_12
    ADD CONSTRAINT relation_12_genre_fk FOREIGN KEY ( genre_genre_id )
        REFERENCES genre ( genre_id )
            ON DELETE CASCADE;

ALTER TABLE relation_16
    ADD CONSTRAINT relation_16_game_fk FOREIGN KEY ( game_game_id )
        REFERENCES game ( game_id )
            ON DELETE CASCADE;

ALTER TABLE relation_16
    ADD CONSTRAINT relation_16_platform_fk FOREIGN KEY ( platform_platform_id )
        REFERENCES platform ( platform_id )
            ON DELETE CASCADE;

CREATE SEQUENCE developer_developer_id1_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER developer_developer_id1_trg BEFORE
    INSERT ON developer
    FOR EACH ROW
    WHEN ( new.developer_id1 IS NULL )
BEGIN
    :new.developer_id1 := developer_developer_id1_seq.nextval;
END;
/



-- Oracle SQL Developer Data Modeler Summary Report: 
-- 
-- CREATE TABLE                            11
-- CREATE INDEX                             0
-- ALTER TABLE                             21
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           1
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          1
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- TSDP POLICY                              0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
