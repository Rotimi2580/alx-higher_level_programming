-- Displays average temperature in a city.
SELECT city, AVG(value) AS avg_temp FROM teperatures GROUP BY city ORDER BY avg_temp DESC;
