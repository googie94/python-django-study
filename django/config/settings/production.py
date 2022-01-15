if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        print(path.dirname( path.dirname( path.abspath(__file__) ) ))
        sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ))
        from base import *
    else:
        from .base import *

config_secret_production = json.loads(open(CONFIG_SECRET_PRODUCTION_FILE).read())
DEBUG = False
ALLOWED_HOSTS = config_secret_production['django']['allowed_hosts']
WSGI_APPLICATION = 'config.wsgi.production.application'
DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
    }
}
