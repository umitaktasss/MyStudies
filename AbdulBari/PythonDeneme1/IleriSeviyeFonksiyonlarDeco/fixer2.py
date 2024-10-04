import requests

# Enter your API key here
api_key = '2a3413cd2011ead5981354dbf2c11e9a'

# Fixer.io API URL
url = f'http://data.fixer.io/api/latest?access_key={api_key}'

# Make a request to the API
response = requests.get(url)

# Convert the response to JSON format
data = response.json()

# If our request is successful
if data['success']:
    print("Current Exchange Rates:")
    # List the exchange rates
    for currency, rate in data['rates'].items():
        print(f"1 EUR = {rate} {currency}")
else:
    # If the request failed, print the error
    print(f"Error: {data['error']['info']}")

