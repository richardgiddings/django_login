#
#   Dev settings
#

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wu--89fy07mx2)&yj3_wsy9)nm-z)=dsjhz*6-13eeuy)1(=#h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
