
-- ! SELECT
SELECT * FROM users where first_name LIKE "K%";
-- selecciona los first_name de users que comienzen con 'K'

SELECT * FROM users where first_name NOT LIKE "%K";
-- selecciona los first_name de users que NO terminen en 'K'

SELECT * FROM users where first_name LIKE "%e" ORDER BY birthday DESC;
-- selecciona los first_name de usuarios que terminen en 'e' con los usuaruis mas jovenes en la parte superior de la tabla,
-- para ordenar y dejar los mas viejos arriba se usa ORDER BY birthday ASC

SELECT first_name FROM users ORDER BY first_name;
-- selecciona los first_name de users y los ordena por orden alfabetico

SELECT * FROM users LIMIT 2, 3;
-- selecciona los usuarios del 3 al 5 (empieza desde 2 y toma 3)

-- ! INSERT
INSERT INTO table_name (column_name1, column_name2) VALUES ('column1_value', 'column2_value');
-- insertar un registro

-- ! UPDATE
UPDATE table_name SET column_name1 = 'some value', column_name2 = 'some other value' WHERE id = 1;
-- actualizar valor en tabla, con WHERE se le puede agregar una condicion

-- ! DELETE
-- Ejecutar SET SQL_SAFE_UPDATES = 0; si hay algun error respescto a la actualizacion de seguridad SQL
DELETE FROM table_name WHERE condicion
-- si no se agrega WHERE se borran todos los registros de la tabla
