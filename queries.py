import requests
import constants 
from datetime import datetime, timezone
import json
import csv


api_url_1 = "https://restcountries.com/v3.1/all"
api_url_2 = "https://api.open-meteo.com/v1/forecast"


# Show top n countries by population
def getByDescPopulation(n):
    search_url = f"{api_url_1}?fields=name,population"
    response = requests.get(search_url)
    if response.status_code == 200:
        countries = response.json()

        sorted_countries = sorted(countries, key=lambda x: x['population'], reverse=True)
    
        top_countries = sorted_countries[:n]

        rank_index = 1
        for country in top_countries:
            name = country['name']['common']
            population = country['population']
            population_str = f"{population:,}"  # Format population with commas
            print(f"{rank_index} - {name:>20}: {population_str:>20}")
            rank_index += 1 
    else:
        print(f"Error: Unable to fetch data, status code {response.status_code}")   
    return


# Show countries that speak a given language
def getByLanguage(lang):
    
    
    search_url = f"{api_url_1}?fields=name,languages"
    response = requests.get(search_url)
    if response.status_code == 200:
        countries = response.json()

        filtered_countries = []
        for country in countries:
            if lang in country['languages'].values():
                filtered_countries.append(country['name']['common'])

        filtered_countries.sort()
        
        print(f"Countries that speak {lang}:")
        
        length = len(filtered_countries)
        index = 0
        for country in filtered_countries:
            print(f"{country}", end="")
            if (index < length - 1):
                print(", ", end="")
            else:
                print("")
            index += 1

    else:
        print(f"Error: Unable to fetch data, status code {response.status_code}")   
    return


# List countries in the Southern Hemisphere
def getByHemisphere(hemisphere: str):
    """Retrieves all countries and lists those in the specified hemisphere (Northern or Southern).

    Args:
        hemisphere (str): _description_
    """
    hemisphere = hemisphere.lower()
    if hemisphere not in constants.hemishperes:
        print("Please specify either 'northern' or 'southern' hemisphere.")
        return
    
    qry = f"{api_url_1}?fields=name,latlng"
    response = requests.get(qry)
    print(f"Countries in the {hemisphere} Hemisphere:")
    if response.status_code == 200:
        countries = response.json()
        for country in countries:
            latlng = country['latlng']
            if hemisphere == "southern" and latlng[0] < 0:
                print(country['name']['common'])
            elif hemisphere == "northern" and latlng[0] > 0:
                print(country['name']['common'])
    
    return 
    

# Find the country with the longest name
def getByLongestName():
    """Retrieves all countries and finds the one with the longest name.
    
    """

    qry = f"{api_url_1}?fields=name"
    response = requests.get(qry)
    print("Country with the longest name:")
    if response.status_code == 200:
        countries = response.json()
        max = 0
        longestCountry = ""
        
        # Iterate through the countries to find the longest name
        for country in countries:
            name_length = len(country['name']['common'])
            if name_length > max:
                max = name_length
                longestCountry = country['name']['common']
        
        print(longestCountry)
    return


# Calculate the average population across all countries
def getAveragePopulation():
    """ Retrieves all countries and calculates the average population.
    """
    qry = f"{api_url_1}?fields=name,population"
    response = requests.get(qry)
    
    print("Average population across all countries:")
    if response.status_code == 200:
        countries = response.json()
        total_population = 0
        
        for country in countries:
            total_population += country['population']        
        
        average_population = total_population / len(countries)
        print(average_population)
    
    return


# Show current temperature of location accessed via latitude/longitude
def getCurrTemp(lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    response = requests.get(api_url_2, params=params)

    if response.status_code == 200:
        data = response.json()
        current_weather = data.get("current_weather", {})
        temperature = current_weather.get("temperature")
        print(f"Current temperature at {lat}, {lon}: {temperature}°C")
    
    return


# Show current precipitation of location accessed via latitude/longitude
def getCurrPrecip(lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "precipitation",
        "current_weather": True,
    }

    response = requests.get(api_url_2, params=params)

    data = response.json()

    # Get current time rounded down to the hour 
    now_utc = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)
    now_str = now_utc.strftime("%Y-%m-%dT%H:%M")

    times = data.get("hourly", {}).get("time", [])
    precipitation_values = data.get("hourly", {}).get("precipitation", [])


    # Find index of current hour 
    idx = times.index(now_str)
    precip = precipitation_values[idx]

    print(f"Current precipitation at {lat}, {lon}: {precip} mm")

    return


# Save all countries to a file
def getAllCountries(format, path):
    filePath = f"{path}.{format}"
    search_url = f"{api_url_1}?fields=name"
    response = requests.get(search_url)
    
    if response.status_code == 200:
        countries = response.json()

        country_names = []
        for country in countries:
            country_names.append(country['name']['common'])
        country_names.sort()

        if format == "json":
            with open(filePath, 'w') as json_file:
                json.dump(country_names, json_file, indent=4)
            print("Countries saved to countries.json")
        elif format == "csv":
            with open(filePath, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                for country in country_names:
                    writer.writerow([country])
            print(f"Countries saved to {filePath}")
        else:
            print("Invalid format specified. Use 'json' or 'csv'.")
    else:
        print(f"Error: Unable to fetch data, status code {response.status_code}")   
    return
