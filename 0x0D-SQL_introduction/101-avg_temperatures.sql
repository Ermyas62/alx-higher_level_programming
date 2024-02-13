-- Displays the average tempreture
-- City orderd by descending temprature
SELECT `city`, AVG(`value`) as `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
