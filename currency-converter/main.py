from clients import CoinConvertorService


if __name__ == '__main__':
    client = CoinConvertorService()
    conversion = client.convert(coin_origin='BTC', coin_target='BRL')

    print('Conversion: ', conversion)
