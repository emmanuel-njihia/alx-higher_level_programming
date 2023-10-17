-- This script lists the number of records with the same score in the table second_table in my MySQL server.
-- order in descending count.
SELECT `score`, COUNT(*) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
