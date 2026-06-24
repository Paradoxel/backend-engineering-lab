import requests  # import HTTP library

BASE_URL = "https://open.er-api.com/v6/latest/"  # base API endpoint

# get user input
from_currency = input("From currency: ").upper()
to_currency = input("To currency: ").upper()
amount = float(input("Amount: "))

# build API URL
url = BASE_URL + from_currency

# call API
response = requests.get(url)
data = response.json()

# check API success
if response.status_code != 200:
    print("API Error")
    exit()

# get rates dictionary
rates = data.get("rates", {})

# validate target currency
if to_currency in rates:
    rate = rates[to_currency]  # exchange rate

    result = amount * rate  # conversion logic

    # output result
    print(f"\n{amount} {from_currency} = {result:.2f} {to_currency}")

else:
    print("Invalid currency")