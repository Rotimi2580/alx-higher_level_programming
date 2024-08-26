-- A code to print only selected objexts in SQL with name value.
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != ''ORDER BY score DESC;
