from celery import shared_task
from cryptocompy import price
from django.core.cache import cache
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@shared_task
def update_cc_prices():
    cryptocoins = ['ETH', 'BTC']
    currencies = ['EUR', 'USD']
    response = price.get_current_price(cryptocoins, currencies)
    channel_layer = get_channel_layer()
    for cryptocoin in cryptocoins:
        for currency in currencies:
            latest_price = response[cryptocoin][currency]
            ticker_code = cryptocoin + currency
            if cache.get(ticker_code) != latest_price:
                cache.set(ticker_code, response[cryptocoin][currency])
                async_to_sync(channel_layer.group_send)(
                    ticker_code,
                    {
                        'type': 'price_update',
                        'price': latest_price,
                    }
                )
