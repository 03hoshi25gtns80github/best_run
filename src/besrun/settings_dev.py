from .settings_common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    
    # ロガーの設定
    'loggers': {
        # Django
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # MyBestRun
        'MyBestRun': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
    
    # ハンドラ 
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev',
        },
    },
    # フォーマッタ
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    },
}

