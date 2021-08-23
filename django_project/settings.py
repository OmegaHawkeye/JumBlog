import os
from pathlib import Path
from decouple import config
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = config('DEBUG',cast=bool,default=False)

ADMINS = [('Julian Chornitzer','chornitzerj@gmail.com')]

MANAGERS = ADMINS

ALLOWED_HOSTS = ['127.0.0.1','jumblog.herokuapp.com','jumblog-dev.herokuapp.com','jumblog-production.herokuapp.com']
        
INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'core',
    'users.apps.UsersConfig',
    'support',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_email_verification',
    'debug_toolbar',
    'taggit',
    'django_comments_xtd',
    'django_comments',
    'bootstrap_datepicker_plus',
    'imagekit',
    'admin_honeypot',
    'django_extensions',
    'tellme',
    'friendship',
    'tinymce', 
    # 'gTTS',
    'hitcount',
    'django_countries',
    'django_social_share', 
]

SITE_ID = 2

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INTERNAL_IPS = [ '127.0.0.1' ]

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_project.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':   config("DB_NAME"), 
        'USER':    config("DB_NAME"), 
        'PASSWORD': config("DB_NAME"), 
        'HOST':  config("DB_NAME"),
        'PORT': config("DB_NAME"),
        }   
    }      

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = "users.CustomUser"

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Vienna'

USE_I18N = True

USE_L10N = True

USE_TZ = False

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

CRISPY_TEMPLATE_PACK = 'bootstrap5'

BOOTSTRAP4 = {
    'include_jquery': False,
}

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'landing'

def verified_callback(user):
    user.is_active = True

EMAIL_VERIFIED_CALLBACK = verified_callback
EMAIL_FROM_ADDRESS = 'jumblogoffice@gmail.com'
EMAIL_MAIL_SUBJECT = 'Confirm your email'
EMAIL_MAIL_HTML = 'email_confirm/mail_body.html'
EMAIL_MAIL_PLAIN = 'email_confirm/mail_body.txt'
EMAIL_TOKEN_LIFE = 60 * 60
EMAIL_PAGE_TEMPLATE = 'email_confirm/confirm_template.html'

EMAIL_PAGE_DOMAIN = 'https://jumblog.herokuapp.com'
    
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = config("EMAIL_HOST_USER")

EMAIL_HOST_PASSWORD  = config("EMAIL_HOST_PASSWORD")

AWS_STORAGE_BUCKET_NAME =config("AWS_STORAGE_BUCKET_NAME")

AWS_SECRET_ACCESS_KEY =config("AWS_SECRET_ACCESS_KEY")

AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")

AWS_URL = config("AWS_URL")

AWS_S3_REGION_NAME = config("AWS_S3_REGION_NAME")

AWS_S3_SIGNATURE_VERSION = config("AWS_S3_SIGNATURE_VERSION")

AWS_DEFAULT_ACL = None

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_URL = AWS_URL + '/static/'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = AWS_URL + '/media/'
DEFAULT_FILE_STORAGE = 'django_project.storage_backends.MediaStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

COMMENTS_APP = 'django_comments_xtd'
COMMENTS_XTD_MAX_THREAD_LEVEL_BY_APP_MODEL = {
        'core.article': 4,
        'support.ticket':3
}

COMMENTS_XTD_CONFIRM_EMAIL = True

COMMENTS_XTD_APP_MODEL_OPTIONS = {
    'default': {
        'allow_flagging': True,
        'allow_feedback': True,
        'show_feedback': True,
        'who_can_post': 'users'
    }
}

sentry_sdk.init(
    dsn=config("SENTRY_DSN"),
    integrations=[DjangoIntegration()],
    traces_sample_rate=0.5,
    send_default_pii=True
)
