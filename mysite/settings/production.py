import os
import dj_database_url

from .base import *


env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

DEBUG = False

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'

try:
    from .local import *
except ImportError:
    pass

# This is to allow debugging if heroku gives no info in logs
# It should be enabled temporarily only when required
# because we are checking an 'environment variable' on heroku
# to see if debug mode should be enabled, once this is deployed can 
# enable by setting heroku config in UI or CLI:
# heroku config:set DJANGO_DEBUG=True
if "DJANGO_DEBUG" in env:
    DEBUG = env["DJANGO_DEBUG"]