"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""


from config.settings import *  # noqa


SPECTACULAR_SETTINGS = {
    'TITLE': 'new point+plus API terminal',
    'DESCRIPTION': '店舗端末用API',
    'VERSION': '1.0.0',
    'SCHEMA_PATH_PREFIX': '/terminal/api/v[0-9]',
    'SCHEMA_PATH_PREFIX_TRIM': True,

    'SERVERS': [
        {
            'url': 'https://localhost:8000/terminal/api/v1',
            'description': 'Local'
        }
    ],

    'PREPROCESSING_HOOKS': [
        'open_api.preprocessing.terminal_preprocessing_hook',
        'drf_spectacular.hooks.preprocess_exclude_path_format'
    ]
}
