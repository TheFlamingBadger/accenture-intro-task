emptyInputString = "Enter a command. Use 'help' to see available commands."

unknownCmdString = "Unrecognised command. Use 'help' to see available commands."

helpString = """
Available Commands:

1. help — list commands
2. top-population [num countries] — show top n countries by population
3. language [lang] — show countries that speak a given language
4. save --format [json|csv] --path [path] — save all countries to a file
5. hemisphere [southern|northern] — list countries in the Southern Hemisphere
6. longest-name — list country with the longest name
7. avg-population — show avg population of all countries
8. temperature [lat] [lon] - show current temperature of location accessed via latitude/longitude
9. precipitation [lat] [lon] - show current temperature of location accessed via latitude/longitude
"""

hemishperes = ["northern", "southern"]
defaultType = "json"
defaultPath = "countries"