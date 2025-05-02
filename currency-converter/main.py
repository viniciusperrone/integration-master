import requests


BASE_URL = 'https://economia.awesomeapi.com.br/json/last'

def convert(coin_origin, coin_target):
    response = requests.get(
        url=f'{BASE_URL}/{coin_origin}-{coin_target}'
    )
    
    if response.status_code == 404:
        return response.json().get("message")
    return response.json().get(f'{coin_origin}{coin_target}').get('bid')

if __name__ == '__main__':
    result = convert('BTC', 'BRL')
    print(result)