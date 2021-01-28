"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 1.11.12.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_DIR)
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&+%a5u2*@it7)&mj_jz1!me=d5_#hps+d4_3=a(0_pk&#df8g!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1','112.124.6.9',]

AUTH_USER_MODEL = 'users.UserProfile'

# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'users.apps.UsersConfig',
    'blog.apps.BlogConfig',
    'comment.apps.CommentConfig',
    #'blog',
    #'django.contrib.humanize', # 添加人性化过滤器
    #'apps.templatetags',#注册自动以过滤器和标签
    'xadmin', 
    'crispy_forms',
    'reversion',

    'django.contrib.humanize',

    'allauth.socialaccount.providers.weixin', # 微信
    'allauth.socialaccount.providers.github', # 微信
    'allauth.socialaccount.providers.weibo', # 微信

]

SITE_ID = 1

#基本设定
ACCOUNT_AUTHENTICATION_METHOD = 'username'#用户登录方法
LOGIN_REDIRECT_URL = '/'#用户登录后跳转链接
ACCOUNT_LOGOUT_REDIRECT_URL = "/" #设置退出登录后跳转链接
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5 #登录尝试失败的次数


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# 全文搜索应用配置
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'blog.whoosh_cn_backend.WhooshEngine',  # 选择语言解析器为自己更换的结巴分词
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),  # 保存索引文件的地址，选择主目录下，这个会自动生成
    }
}
# 统一分页设置
BASE_PAGE_BY = 10
BASE_ORPHANS = 5


HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'myblog.wsgi.application'



# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Xyw@172410',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'  # 中文支持，django1.8以后支持；1.8以前是zh-cn

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False  # 默认是Ture，时间是utc时间，由于我们要用本地时间，所用手动修改为false！！！！



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, '/staticcoll')

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#网站默认设置和上下文信息
SITE_DESCRIPTION = '网站描述'

LOGIN_URL='/'

# 表单插件的配置
CRISPY_TEMPLATE_PACK = 'bootstrap4'

#邮箱设定
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER =  # 你的邮箱账号
EMAIL_HOST_PASSWORD =  # 这里是邮箱提供给的授权码，不是个人密码
EMAIL_USE_TLS = True  # 保持不变
EMAIL_FROM =  # 你的邮箱账号
DEFAULT_FROM_EMAIL = '

SITE_END_TITLE = '一个基于Github：https://github.com/Hopetree的个人博客'
SITE_DESCRIPTION = ''
SITE_KEYWORDS = ''
