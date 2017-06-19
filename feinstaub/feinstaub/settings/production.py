#
# TODOs
#
# rename this file to production.py
#

from .base import *

DEBUG = True

# add your host here:
ALLOWED_HOSTS = ['*']

STATIC_ROOT = '/home/uid1000/feinstaub/static/'
USE_X_FORWARDED_HOST = True

# set a new secret key:
SECRET_KEY = '%_qp8x233p&#zrt1y1v_kgp0a6ryj6(9&rr&j!f=xfyv1p%gg8'

# set some secrets for APIs
FORECAST_IO_KEY = '%_qp8x233p&#zrt1y1v_kgp0a6ryj6(9&rr&j!f=xfyv1p%gg8'
