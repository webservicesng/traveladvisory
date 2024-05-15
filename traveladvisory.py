

import requests
import json

def get_country_info(country_code):
    url = f"(link unavailable)"
    response = requests.get(url)
    data = response.json()
    return data

def write_to_json(data, data_json_info):
    with open(data_json_info, 'w') as file:
        json.dump(data, file, indent=4)

def print_country_info(data):
    country = data["data"][0]
    print(f"Country: {country['name']}")
    print(f"ISO Alpha2: {country['iso_alpha2']}")
    print(f"Continent: {country['continent']}")
    print(f"Advisory Score: {country['Advisory']['score']}")
    print(f"Advisory Message: {country['Advisory']['message']}")

def main():
    country_code = input("Enter a two-letter ISO country code: ")
    data = get_country_info(country_code)
    write_to_json(data, f"{country_code}.json")
    print_country_info(data)

if __name__ == "__main__":
    main()