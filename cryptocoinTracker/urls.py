from django.urls import path

from .views import TickerView

urlpatterns = [
    path('', TickerView.as_view()),
]

from .consumers import TickerConsumer
websocket_urlpatterns = [
    path('ws/<str:cryptocoin>/<str:currency>', TickerConsumer),
]