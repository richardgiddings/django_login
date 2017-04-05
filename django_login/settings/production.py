#
#   Production settings
#

from .base import *

import os

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

DEBUG = False

EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Admin <noreply@example.com>'