#Library

#pip3 install requests
#pip3 install pandas
#pip install tradingview-ta
#pip install tvdatafeed

################

#Import required
import datetime 
import pandas as pd
import time as t
import random as rd
import requests as rq
import logging as lg
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup

#XAU
def web_content_div(web_content, class_path):
    web_content_div = web_content.find_all('div', {'class':class_path})
    try:
        spans = web_content_div[0].find_all('span')
        texts = [span.get_text() for span in spans]
    except IndexError:
        texts =[]
        return texts


def real_time_price(stock_code):
    url = 'https://vn.investing.com/currencies/' + stock_code
    try:
        r = rq.get(url)
        web_content = BeautifulSoup(r.text,'lxml')
        texts = web_content_div(web_content, 'instrument-price_instrument-price__2w9MW flex items-end flex-wrap font-bold')
        if texts != []:
            price, change = texts[0],texts[1]
        else:
            price, change = [], []
    except ConnectionError:
        price, change = [], []
    return price, change 
stock_code = ['xau-usd']



# API access and Cryptos

# API key and secret
API_KEY = "fill in your API Key"
API_SECRET = "fill in your API secret"

# Logging
lg.basicConfig(level=lg.INFO)

# Get the current Bitcoin/USD price
def get_bitcoin_price():
    endpoint = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = rq.get(endpoint, headers={"API_KEY": API_KEY, "API_SECRET": API_SECRET})

    if response.status_code == 200:
        return response.json()["price"]
    else:
        raise Exception("Error: Could not get Bitcoin price")

# Get the current ETH/USD price
def get_ETH_price():
    endpoint = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
    response = rq.get(endpoint, headers={"API_KEY": API_KEY, "API_SECRET": API_SECRET})

    if response.status_code == 200:
        return response.json()["price"]
    else:
        raise Exception("Error: Could not get ETH price")

# Get the current BNB/USD price
def get_BNB_price():
    endpoint = "https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT"
    response = rq.get(endpoint, headers={"API_KEY": API_KEY, "API_SECRET": API_SECRET})

    if response.status_code == 200:
        return response.json()["price"]
    else:
        raise Exception("Error: Could not get BNB price")


# List of tracking Cryptos
list_crypto = ["ETH", "BNB"]

# Identify the current time
time_now = t.strftime("%Y-%m-%d %H:%M:%S")

# Work can do
do_list = ["1. food", "2. time", "3. interest rate calculation", "4. Bitcoin price", "5. other Crypto prices", "6. AUX/USD"]

# Create a list of foods
food = ["Pizza", "Hủ Tiếu", "Phở", "Bánh mì", "Burger"]

# Get the user's name
name = input("What is your name? ")

# Print a greeting
print("Hi, {}!".format(name))

# Choices of helps
print("I can help you with {}.".format(do_list))

# Ask the user what they want
command = input("How can I help you? ")

# Check if the user wants to know the current time
if "time" in command or "2" in command:
    print("Currently, ",time_now)

# Check if the user wants to get a random food
if "food" in command or "1" in command:
    print(rd.choice(food))

# Check if the user wants to help do the calculation
if "interest rate calculation" in command or "3" in command:
    print("Please fill in")
    #interest rate calculation

    P0 = int(float(input("Please fill in your initial deposit $")))
    I = int(float(input("Please fill in your annualy interest rate %")))

    type = input("what kind of periods you want to do: 1. week, 2. month, 3. year ?")
    if "week" in type or "1" in type:
        n = float(input("Please fill in number of weeks"))
    elif "month" in type or "2" in type:
        n = float(input("Please fill in number of months"))
    elif "year" in type or "3" in type:
        n = float(input("Please fill in number of years"))

    if "week" in type or "1" in type:
        I = int(float(I)) / 52
    elif "month" in type or "2" in type:
        I = int(float(I)) / 12
    elif "year" in type or "2" in type:
        I = int(float(I))

    FV = int(P0 * (1+I/100) ** int(n))

    print("Here is the money you will receive $", FV)
    
# Check if the user wants to know the current Bitcoin price
if "Bitcoin price" in command or "4" in command:
    print("The current price of Bitcoin is: ${}".format(get_bitcoin_price()))

# Check if the user wants to know the other current Crypto price
if "other Crypton prices" in command or "5" in command:
    print("Here are list of crypto you can track: ", list_crypto)
    crypto = input ()
    if "ETH" in crypto or "1" in crypto:
        print("The current price of ETH is: ${}".format(get_ETH_price()))
    elif "BNB"in crypto or "2" in crypto: 
        print("The current price of BNB is: ${}".format(get_BNB_price()))

# Check if the user wants to know the other current AUX/USD price
if "Gold" in command or "6" in command or "AUX/USD" in command:
    print("This is the current AUX/USD", real_time_price('aux-usd'))