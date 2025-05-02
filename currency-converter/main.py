from clients.convertor_service import CoinConvertorService
from clients.callmebot_service import CallMeBotService


if __name__ == '__main__':
    client = CoinConvertorService()
    conversion = client.convert(coin_origin='BTC', coin_target='BRL')

    wpp_service = CallMeBotService()
    response = wpp_service.send_message(
        message=f'Cotação do Bitcoin: R$ {conversion}'
    )
