import requests

curl_response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/usd.json')
#print(type(curl_response))
data_dict = curl_response.json()
#print(type(data_dict))
print('Bitcoin price in USD:')
print(data_dict["bpi"]["USD"]["rate"])