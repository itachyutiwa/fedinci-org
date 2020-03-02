import dj_database_url
from .settings import *

DEBUG=False
TEMPLATE_DEUG=False
DATABASES['default'] = dj_database_url.config()
MIDDLEWARE+=['whitenoise.middleware.WhiteNoiseMiddleware']
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
SECRET_KEY = 'lxzx2@%a*yey1$ca(94a%h-#qi=&6a%$ce((pp%naf4#gsgebr'
ALLOWED_HOSTS =['fedinci-org.herokuapp.com']