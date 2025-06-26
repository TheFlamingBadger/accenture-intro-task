import requests


api_url_1 = "https://restcountries.com/v3.1/all"


# ./countrytool top-population [n] — show top n countries by population
#JUSTINE
def getByDescPopulation(n):
    search_url = f"{api_url_1}?fields=name,population"
    response = requests.get(search_url)
    if response.status_code == 200:
        countries = response.json()
        print("Countries")
        print(countries)

        sorted_countries = sorted(countries, key=lambda x: x['population'], reverse=True)
        print("Sorted Countries")
        print(sorted_countries)
    
        top_countries = sorted_countries[:n]
        print("Top Countries")
        print(top_countries)
        
    else:
        print(f"Error: Unable to fetch data, status code {response.status_code}")   
    return

# ./countrytool language [lang] — show countries that speak a given language
#JUSTINE
def getByLanguage(lang):
    return

# ./countrytool southern — list countries in the Southern Hemisphere
#JUSTINE
def getByHemisphere(hemisphere):
    return

# ./countrytool longest-name — find the country with the longest name
#QUENTON
def getByLongestName():
    return

# ./countrytool average-population — calculate the average population across all countries
#QUENTON
def getAveragePopulation():
    return


if __name__ == "__main__":
    # Example usage
    n = 5  # Change this to the number of top countries you want to see
    getByDescPopulation(n)
    # getByLanguage("English")
    # getByHemisphere("Southern")
    # getByLongestName()
    # getAveragePopulation()