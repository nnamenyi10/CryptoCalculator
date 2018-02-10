import requests
import math

r = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=10')

coins = []
values = []
inf = math.inf

for coin in r.json():
    coins.append(coin['symbol'])
    values.append(coin['price_usd'])

# create a dictionary from the lists
currencyDict = dict()
for i in range(0, len(coins)):
    # if a key is not in the dictionary, it will create it automatically
    currencyDict[coins[i]] = values[i]

print('Hello! Welcome to the USD -> top 10 Cryptocurriencies Calculator!\n')

#amount of dollars that need converted
def input_amount():
    while True:
        try:
            amount = float(input("How many Dollars(USD) would you like to convert?\n" + '$'))
            if not (0.01 <= amount <= inf):
                raise ValueError()

        except ValueError:
            print('that\'s not a number I can work with! haHAA')

        else:
            return amount
            break

#what I am converting to
def input_symbol():
    while True:
        try:
            currency = input("Into which Coin?\n")
            if currency not in coins:
                raise ValueError()
        except ValueError:
            print("The currency you entered is invalid, use one of these symbols: " + '\n' + str(coins))

        else:
            return currency
            break

#function to do the converting for me
def usd_to_currency(amount, currency):
    return round(amount / float(currency), 5)


#final result function
def final_result():
    print('---------------------------------')
    print('$'+ str(amount) + ' USD is worth ' + str(usd_to_currency(amount, currencyDict[currency])) + ' ' + currency + '.')
    print('Each coin is worth $' + currencyDict[currency])

#calling the 2 functions I need
amount = input_amount()
currency = input_symbol()

#calling the final result
if currency in currencyDict.keys():
    final_result()
