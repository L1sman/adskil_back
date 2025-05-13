from client_module.settings import global_settings
from .global_settings import *


BASE_DIR = global_settings.BASE_DIR
DEBUG = global_settings.DEBUG
ALLOWED_HOSTS = ['*']
CORS_ALLOW_ALL_ORIGINS = True

try:
    from client_module.settings import local_settings
    DATABASES = local_settings.DATABASES
except ImportError as ex:
    print(ex)

