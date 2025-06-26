# Accenture Intro Task

## Requirements

1. 
https://restcountries.com/

Use this API to:
- List the 10 countries with the highest population.
- Find the countries in the Southern Hemisphere (lat/lng).
- Find the country with the longest name.
- List all countries that speak Spanish.
- Calculate the average population across all countries.

2.
https://api.open-meteo.com/

Use this api to find the following information of a location:
- Current temperature of location
- Precipitation status of location

3.
Combine functionality from both APIs to return geo and weather information for searched location

4.
Make a terminal CLI tool for these scripts. For example, make these commands possible (example with an entry script is called countrytool):

./countrytool top-population [n] — show top n countries by population
./countrytool language [lang] — show countries that speak a given language
./countrytool save --format json|csv --output countries.json — save all countries to a file
./countrytool southern — list countries in the Southern Hemisphere
./countrytool help — show help text
