import logging
import os

from logging.config import dictConfig

logs_path = os.path.join(os.path.dirname(__file__), 'logs')

LOGGING_CONFIG = {
    'version': 1,
    'loggers': {
        '': {  # root logger
            'level': 'NOTSET',
            'handlers': [
                'debug_console_handler',
                'info_rotating_file_handler',
                'error_file_handler',
            ],
        },
        'my.package': {
            'level': 'NOTSET',
            'propagate': False,
            'handlers': [
                'my_mongodb_handler',
                'debug_console_handler',
                'my_info_rotating_file_handler',
                'my_error_file_handler',
                # 'critical_mail_handler'
            ]
        }
    },
    'handlers': {
        'my_mongodb_handler': {
            'level': 'INFO',
            'class': 'log4mongo.handlers.BufferedMongoHandler',
            'host': 'localhost',
            'port': 27017,
            'database_name': 'flask-gunicorn-log',
            'capped': True,
            'buffer_size': 100,
            'buffer_periodical_flush_timing': 10.0,
            'buffer_early_flush_level': logging.ERROR
        },
        'debug_console_handler': {
            'level': 'DEBUG',
            'formatter': 'info',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
        'info_rotating_file_handler': {
            'level': 'INFO',
            'formatter': 'info',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(logs_path, 'info.log'),
            'mode': 'a',
            'maxBytes': 1048576,
            'backupCount': 10
        },
        'my_info_rotating_file_handler': {
            'level': 'INFO',
            'formatter': 'info',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(logs_path, 'my.info.log'),
            'mode': 'a',
            'maxBytes': 1048576,
            'backupCount': 10
        },
        'error_file_handler': {
            'level': 'WARNING',
            'formatter': 'error',
            'class': 'logging.FileHandler',
            'filename': os.path.join(logs_path, 'error.log'),
            'mode': 'a',
        },
        'my_error_file_handler': {
            'level': 'WARNING',
            'formatter': 'error',
            'class': 'logging.FileHandler',
            'filename': os.path.join(logs_path, 'my.error.log'),
            'mode': 'a',
        },
        'critical_mail_handler': {
            'level': 'CRITICAL',
            'formatter': 'error',
            'class': 'logging.handlers.SMTPHandler',
            'mailhost': 'localhost',
            'fromaddr': 'monitoring@domain.com',
            'toaddrs': ['qa@domain.com',],
            'subject': 'Critical error with application name'
        }
    },
    'formatters': {
        'info': {
            'format': '%(asctime)s-%(levelname)s-%(name)s::%(module)s|'
                      '%(lineno)s:: %(message)s'
        },
        'error': {
            'format': '%(asctime)s-%(levelname)s-%(name)s-%(process)d'
                      '::%(module)s|%(lineno)s:: %(message)s'
        },
    }
}

dictConfig(LOGGING_CONFIG)
