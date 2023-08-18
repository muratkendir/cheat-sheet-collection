# OracleDB vs PostgreSQL - Tips and Tricks

## OracleDB - Clauses and the orders

- In OracleDB:
-- INSERT INTO must be declared before the WITH clause.
-- Every (real) table must be called with it's SCHEMA name.
-- Every (real) table must be shorten without AS conjunction.
-- Don't use Aliases in GROUP BY clause (?).
-- If DUAL needed, call it firstly (?).
-- User 0/1 rather than True/False.
-- Try to not use quotation with table names (Use with schema names).
-- Donot use double colon as type casting. Always use CAST(column AS type) expression.

## JSON Array Aggragation and CONCAT

**Command in PostgreSQL** | **Command in OracleDB**
--- | ---
ARRAY_AGG | JSON_ARRAYAGG
anyarray[1] | JSON_VALUE(anyarray, '$[0]')
CONCAT(1,2,3) = '123' | CONCAT(CONCAT(1,2),3)='123'
ST_Envelope(geometry) | SDO_GEOM_MBR(geometry)

## Unsolved issues

**Solution in PostgreSQL** | **Solution in OracleDB**
--- | ---
json_build_object() | JSON_OBJECT?
array | STRARRAY?
unnest & array_position | unsolved