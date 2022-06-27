from django.urls import path
from .consumers import ws_consumer

# Set the path to call the consumer
ws_urlpatterns = [
    path('', ws_consumer.as_asgi()),
]