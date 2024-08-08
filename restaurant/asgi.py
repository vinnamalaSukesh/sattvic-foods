import os
from django.core.asgi import get_asgi_application
from django.urls import re_path
from . import consumer
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant.settings')

django_asgi_app = get_asgi_application()

websocket_urlpatterns = [
    re_path(r"^ws/Order/$", consumer.Order.as_asgi()),
]

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
    }
)