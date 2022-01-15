from .base import *

config_secret_development = json.loads(open(CONFIG_SECRET_DEVELOPMENT_FILE).read())

DEBUG = True
ALLOWED_HOSTS = config_secret_development['django']['allowed_hosts']
WSGI_APPLICATION = 'config.wsgi.development.application'

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   }
}