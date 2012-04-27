from defaults import *

SECRET_KEY = ')r*512d8oit@bu#f$(_0=^oggxs6s20axd328w+4)+-6a5gyv+'

INSTALLED_APPS += (
    'django.contrib.comments',
    'app.timesheet',
    'app.ext',
)  
MIDDLEWARE_CLASSES += (
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'app.urls'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('Jay Zawrotny', 'jayzawrotny@gmail.com'),
)

MANAGERS = ADMINS

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'app.wsgi.application'

DATETIME_FORMAT = 'F j, Y h:i:s a'
TIME_FORMAT = '%I:%H %p'
