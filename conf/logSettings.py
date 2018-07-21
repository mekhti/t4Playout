import os

BASEPATH = os.path(os.path.abspath("manage.py"))

LOGGING = {
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'logfile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(
                BASEPATH, 'logs', 'manage_commands.log'),
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'logfile'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['console', 'logfile'],
            'propagate': False,
            'level': 'ERROR',  # WARN also shows 404 errors
        },
    }
}