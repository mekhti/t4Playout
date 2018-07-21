import os
import logging

BASEPATH =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[Level: %(levelname)s]\n '
                      '\t\t[Logger: %(name)s]\n'
                      '\t\t[Time: %(asctime)s]\n '
                      '\t\t[Module: %(module)s]\n '
                      '\t\t[PID: %(process)d]\n '
                      '\t\t[Thread: %(thread)d]\n '
                      '\t\tMESSAGE:\n \t\t\t%(message)s'
        },
        'simple': {
            'format': '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASEPATH, 'logs', 'manage_commands.log'),
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'manage': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}
