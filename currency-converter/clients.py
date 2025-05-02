import requests


class CoinConvertorService:
    
    def __init__(self):
        self.__base_url = 'https://economia.awesomeapi.com.br/json/last'


    def convert(self, coin_origin, coin_target):
        response = requests.get(
            url=f'{self.__base_url}/{coin_origin}-{coin_target}'
        )
        
        if response.status_code == 404:
            return response.json().get("message")
        
        return response.json().get(f'{coin_origin}{coin_target}').get('bid')
