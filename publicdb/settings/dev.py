from .base import *

print("----USING DEV SETTINGS-----")

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += (
    'debug_toolbar',
    )
