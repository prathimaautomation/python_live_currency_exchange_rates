## Task to ask the user to input any currency code and present the user back the live currency exchange rate
- Let's create a file live_currencyEx.py
```python
import json
import requests

class Live_Currency_EX:

    def read_live_rate_from_api(currency_code):
        #using the currency exchange api along with apikey to get response
        with open('secret.txt') as f:
            key = f.readline()
        url = f"https://free.currconv.com/api/v7/convert?q={currency_code}_PHP&compact=ultra&apiKey={key}"
        #get the response from the api
        check_response = requests.get(url)
        #check if the response is successful
        if check_response.status_code == 200:
            #convert the json response into dictionary to retrieve the required exchange rate
            response_dict = check_response.json()
            return (response_dict[f'{currency_code}_PHP'])
        else:
            print("The currency code is either invalid or unavailable, try again later")

```
- Let's create program.py to call & utilise the Live_Currency_EX methods
```python
from app.live_currencyEX import Live_Currency_EX

#prompting the user for currency code 
currency_input = input("Please enter a currency code for the live exchange rate: ").upper()
#get the live exchange rate from the api by calling Live_Currency_EX class method
live_rate = Live_Currency_EX.read_live_rate_from_api(currency_input)

#present the user back with the live rate
print(f"The live exchange rate of {currency_input} is "+ str(live_rate))
```
#### Output
```python
Please enter a currency code for the live exchange rate: inr
The live exchange rate of INR is 0.657375
```