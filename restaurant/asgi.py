import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
import consumer
from django.urls import re_path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant.settings')

django_asgi_app = get_asgi_application()

websocket_urlpatterns = [
    re_path('/ws/Order/', consumer.Order.as_asgi()),
]

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                websocket_urlpatterns
            )
        )
    ),
})
