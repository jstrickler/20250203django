from .base import *

DEBUG = True

# get common settings from the base settings modulel

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l&i1kefr24%#=(8z%yfcbb!7ud$mc3&b$3q#+ed&p8!b14bj(-'

# When DEBUG is True, Will allow '127.0.0.1', 'LocalHost', and '[::1]'
ALLOWED_HOSTS = []

# add the Django Debug Toolbar
#---------------------------------------------------------------------------
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
INSTALLED_APPS += ['debug_toolbar', ]

INTERNAL_IPS = ['127.0.0.1']

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}
#---------------------------------------------------------------------------


