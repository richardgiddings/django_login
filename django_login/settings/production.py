#
#   Production settings
#

from .base import *

import os

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

DEBUG = False