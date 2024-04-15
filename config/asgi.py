# ruff: noqa
"""
ASGI config for Dev Ops project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/asgi/

"""

import os
import sys
from pathlib import Path

from django.core.asgi import get_asgi_application

# This allows easy placement of apps within the interior
# dev_ops directory.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(BASE_DIR / "dev_ops"))

# If DJANGO_SETTINGS_MODULE is unset, default to the local settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

# If your app don't use websocket use simple asgi application
application = get_asgi_application()
# comment out code bellow this line to use websockets
# This application object is used by any ASGI server configured to use this file.
# django_application = get_asgi_application()

# Import websocket application here, so apps from django_application are loaded first
# from config.websocket import websocket_application


# async def application(scope, receive, send):
#     if scope["type"] == "http":
#         await django_application(scope, receive, send)
#     elif scope["type"] == "websocket":
#         await websocket_application(scope, receive, send)
#     else:
#         msg = f"Unknown scope type {scope['type']}"
#         raise NotImplementedError(msg)
