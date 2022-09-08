DROP DATABASE IF EXISTS SEGORANG;
CREATE DATABASE SEGORANG;
COMMIT;

USE SEGORANG;

CREATE TABLE user(
    id              INT             AUTO_INCREMENT  UNIQUE,
    user_sj_id      VARCHAR(20)     NOT NULL        UNIQUE          PRIMARY KEY,
    user_id         VARCHAR(15)     NOT NULL        UNIQUE,
    user_pw         VARCHAR(20)     NOT NULL,
    user_name       VARCHAR(20)     NOT NULL,
    user_major      VARCHAR(40)     NOT NULL,
    user_nickname   VARCHAR(20)     NOT NULL        UNIQUE,
    is_admin        BOOLEAN         NOT NULL        DEFAULT 0,
    sejong_auth     BOOLEAN         NOT NULL        DEFAULT 0,
    user_create_at  DATETIME        NOT NULL        DEFAULT now()
);