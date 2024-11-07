
import os
from dotenv import load_dotenv

from django.core.asgi import get_asgi_application
load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv("DJANGO_SETTINGS_MODULE", "local"))

application = get_asgi_application()
