import requests
import json
from config import keys


class ConvertionException(Exception):
    pass

class APIException:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if amount.isdigit() is False:
            raise ConvertionException(f'Не удалось обработать количество! {amount}')

        if quote == base:
            raise ConvertionException(f'Вы ввели одинаковые валюты! {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту! {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту! {base}')

        try:
            amount = int(amount)
        except KeyError:
            raise ConvertionException(f'Не удалось обработать количество! {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]] * amount

        return total_base