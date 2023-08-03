CREATE TABLE parametros(
    mp10 integer,
    mp2 integer,
    o3 integer,
    co integer,
    no2 integer,
    so2 integer
);

INSERT INTO parametros(mp10,mp2,o3,co,no2,so2) values (1,2,3,4,5,6)

INSERT INTO parametros(mp10,mp2,o3,co,no2,so2) values (125,236,252,142,856,32)
INSERT INTO parametros(mp10,mp2,o3,co,no2,so2) values (1,2,3,4,5,6)
INSERT INTO parametros(mp10,mp2,o3,co,no2,so2) values (20,5,36,85,41,59)
select * from parametros

SELECT ID FROM parametros
SELECT mp10 FROM parametros WHERE ID = 1
SELECT ID FROM parametros

delete from parametros
alter sequence PARAMETROS_SEQ_ID restart start with 1;