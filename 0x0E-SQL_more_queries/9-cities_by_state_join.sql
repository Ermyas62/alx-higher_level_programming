-- Lists all cities in the database
-- Records are sorted in order of ascending cities.id
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
