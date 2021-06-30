import json
import requests

class Live_Currency_EX:

    def read_live_rate_from_api(currency_code):
        #using the currency exchange api along with apikey to get response
        url = f"https://free.currconv.com/api/v7/convert?q={currency_code}_PHP&compact=ultra&apiKey=393449d779be4f68212b"
        #get the response from the api
        check_response = requests.get(url)
        #check if the response is successful
        if check_response.status_code == 200:
            #convert the json response into dictionary to retrieve the required exchange rate
            response_dict = check_response.json()
            return (response_dict[f'{currency_code}_PHP'])
        else:
            print("The currency code is either invalid or unavailable, try again later")



