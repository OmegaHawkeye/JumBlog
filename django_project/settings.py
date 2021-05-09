import os
from pathlib import Path
from decouple import config
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'm5zywpxsl+tu8$2d(u4_utr+v%)nvii94fc+hj2ixnfr4uwv0w'

DEBUG = False

# ALLOWED_HOSTS = ['*']

# MANAGERS = (
#     ('Julian Chornitzer', 'chornitzerj@gmail.com'),
# )

ADMINS = [('Julian Chornitzer','chornitzerj@gmail.com')]

ALLOWED_HOSTS = ['127.0.0.1', 'jumblog.herokuapp.com']

INSTALLED_APPS = [
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
    'crispy_forms',
    'crispy_bootstrap5',
    'django_email_verification',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.linkedin',
    'debug_toolbar',
    'martor',
    'taggit',
    'django_comments_xtd',
    'django_comments',
]

if DEBUG:
    SITE_ID = 1
else:
    SITE_ID = 2

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
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

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':  "d54ia883272jok",
        'USER':   "mxdhqjnvjbfwlk",
        'PASSWORD': "aa7e43cec1c3562efa6be039384ee39676ae5d539063390d2ca16198c201e2db",
        'HOST':  "ec2-34-247-118-233.eu-west-1.compute.amazonaws.com",
        'PORT': '5432',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

CRISPY_TEMPLATE_PACK = 'bootstrap5'

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

if DEBUG:
    EMAIL_PAGE_DOMAIN = '127.0.0.1:8000'
else:
    EMAIL_PAGE_DOMAIN = 'https://jumblog.herokuapp.com'
    
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'jumblogoffice@gmail.com'

EMAIL_HOST_PASSWORD  = '%rJSjN#96xuF#y^pRv85*jNkF34m'

AWS_STORAGE_BUCKET_NAME = 'jumblog'

AWS_SECRET_ACCESS_KEY = 'YFmO2/IcohZkd++DraMMqV4qy1uGGllZ/DzIouo9'

AWS_ACCESS_KEY_ID = 'AKIAYBOUMUXQFXEAFISG'

AWS_URL = 'https://jumblog.s3.amazonaws.com/'

AWS_S3_REGION_NAME = 'eu-central-1'

AWS_S3_SIGNATURE_VERSION = 's3v4'

AWS_DEFAULT_ACL = None

if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/static/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
else:       
    STATIC_URL = AWS_URL + '/static/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    MEDIA_URL = AWS_URL + '/media/'
    DEFAULT_FILE_STORAGE = 'django_project.storage_backends.MediaStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MARTOR_THEME = 'bootstrap'

MARTOR_ENABLE_CONFIGS = {
    'emoji': 'true',        # to enable/disable emoji icons.
    'imgur': 'true',        # to enable/disable imgur/custom uploader.
    'mention': 'false',     # to enable/disable mention
    'jquery': 'true',       # to include/revoke jquery (require for admin default django)
    'living': 'false',      # to enable/disable live updates in preview
    'spellcheck': 'false',  # to enable/disable spellcheck in form textareas
    'hljs': 'true',         # to enable/disable hljs highlighting in preview
}

MARTOR_TOOLBAR_BUTTONS = [
    'bold', 'italic', 'horizontal', 'heading', 'pre-code',
    'blockquote', 'unordered-list', 'ordered-list',
    'link', 'image-link', 'emoji','toggle-maximize', 'help'
] #'image-upload','direct-mention',

MARTOR_ENABLE_LABEL = True

MARTOR_MARKDOWN_BASE_MENTION_URL = 'http://jumblog.herokuapp.com/' 

# MARTOR_ALTERNATIVE_JS_FILE_THEME = "js/bootstrap.bundle.min.js"
MARTOR_ALTERNATIVE_CSS_FILE_THEME = "css/main.css"

# CSRF_COOKIE_HTTPONLY = False

COMMENTS_APP = 'django_comments_xtd'
COMMENTS_XTD_MAX_THREAD_LEVEL = 2
COMMENTS_XTD_CONFIRM_EMAIL = True

COMMENTS_XTD_APP_MODEL_OPTIONS = {
    'default': {
        'allow_flagging': True,
        'allow_feedback': True,
        'show_feedback': True,
        'who_can_post': 'users'  # Valid values: 'all', users'
    }
}

