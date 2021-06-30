from app.live_currencyEX import Live_Currency_EX

#prompting the user for currency code
currency_input = input("Please enter a currency code for the live exchange rate: ").upper()
#get the live exchange rate from the api by calling Live_Currency_EX class method
live_rate = Live_Currency_EX.read_live_rate_from_api(currency_input)

#present the user back with the live rate
print(f"The live exchange rate of {currency_input} is "+ str(live_rate))