import requests

countrydata= requests.get( "https://restcountries.com/v3.1/all?fields=name,capital,currencies")

print(countrydata.json()
print(json.dumps(countrydata)