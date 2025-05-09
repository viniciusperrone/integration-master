import os
import requests

from dotenv import load_dotenv


load_dotenv()

class CallMeBotService:

    def __init__(self):
        self.__base_url = os.getenv('CALLMEBOT_API_URL')
        self.__api_key = os.getenv('CALLMEBOT_API_KEY')
        self.__phone = os.getenv('CALLMEBOT_PHONE_NUMBER')

    def send_message(self, message):
        response = requests.get(
            url=f'{self.__base_url}?phone=+{self.__phone}&text={message}&apikey={self.__api_key}'
        )

        return response.text
