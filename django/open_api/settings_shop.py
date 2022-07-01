"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""


from config.settings import * # noqa


SPECTACULAR_SETTINGS = {
    'TITLE': 'new point+plus API shop',
    'DESCRIPTION': '店舗Web用API',
    'VERSION': '1.0.0',
    'SCHEMA_PATH_PREFIX': '/shop/api/v[0-9]',
    'SCHEMA_PATH_PREFIX_TRIM': True,

    'PREPROCESSING_HOOKS': [
        'open_api.preprocessing.shop_preprocessing_hook',
        'drf_spectacular.hooks.preprocess_exclude_path_format'
    ],

}
