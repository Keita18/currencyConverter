# Python program to convert the currency
# of one country to that of another country

# Import the modules needed
import requests

class Currency_convertor:
    # empty dict to store the conversion rates
    rates = {}
    def __init__(self, url):
        data = requests.get(url).json()

        # Extracting only the rates from the json data
        self.rates = data["rates"]

