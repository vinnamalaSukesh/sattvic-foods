import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant.settings')

application = get_asgi_application()

ws_patterns = [

]

application = ProtocolTypeRouter({
    'websocket': URLRouter(ws_patterns)
})