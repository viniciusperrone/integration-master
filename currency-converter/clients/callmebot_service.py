import os
import requests

from dotenv import load_dotenv


load_dotenv()

class CallMeBotService:

    def __init__(self):
        self.__base_url = 'https://api.callmebot.com/whatsapp.php'
        self.__api_key = os.getenv('CALLMEBOT_API_KEY')

    def send_message(self, message):
        response = requests.get(
            url=f'{self.__base_url}?phone=554174017213&text={message}&apikey={self.__api_key}'
        )

        return response.text
