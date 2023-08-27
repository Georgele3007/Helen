import time
import random
import requests
import logging

# API key and secret
API_KEY = "Fill in your API_KEY"
API_SECRET = "Fill in your API_SCRET"

# Logging
logging.basicConfig(level=logging.INFO)

# Get the current Bitcoin/USD price
def get_bitcoin_price():
    endpoint = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(endpoint, headers={"API_KEY": API_KEY, "API_SECRET": API_SECRET})

    if response.status_code == 200:
        return response.json()["price"]
    else:
        raise Exception("Error: Could not get Bitcoin price")

bitcoin_price = get_bitcoin_price()

# Identify the current time
time_now = time.strftime("%Y-%m-%d %H:%M:%S")

# Work can do
do_list = ["food", "time", "calculation", "current Bitcoin price"]

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
if "time" in command:
    print(time_now)

# Check if the user wants to get a random food
if "food" in command:
    print(random.choice(food))

# Check if the user wants to help do the calculation
if "calculation" in command:
    print("Please write down your calculation")

# Check if the user wants to know the current Bitcoin price
if "Bitcoin price" in command:
    print("The current price of Bitcoin is: ${}".format(bitcoin_price))
