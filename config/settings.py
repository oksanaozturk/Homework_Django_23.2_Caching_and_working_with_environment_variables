"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

# Перед этим делаем импорт через командную строку pip install python-dotenv  и вносим в requirements.txt
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Настраиваем получение информации по переменным из файла .env
# Эта команда загружает всё из файла .env
load_dotenv(BASE_DIR / ".env")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-@e7dpij2$&b4d1o)0=b@!fy56-$7ay5f3%l^$(5u+ywxdd&s6$"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "catalog",
    "blog",
    "users",
    "phonenumber_field",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# import os
# secret = os.getenv('PASSWORD_POSTGRESQL')
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",  # django.db.backends.postgresql /
        # django.db.backends.postgresql_psycopg2
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        # 'HOST': os.getenv("POSTGRES_HOST"),  # Можно не писать, если стандартный localhost
        # 'PORT': os.getenv("POSTGRES_PORT"),  # Можно не писать, если стандартный
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),  # os.getenv('PASSWORD_POSTGRESQL')
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Отвечает за формирование адреса доступа к статике
STATIC_URL = "static/"

# Отвечает за место на диске, откуда необходимо подгружать статику
STATICFILES_DIRS = (BASE_DIR / "static",)


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Нужны для настройки/работы с документами, которые загружал пользователь (фото, аватарки, видео, аудиофайлф)
# /работают также как и STATIC_URL
# Необходимо создать папку 'media' в корне проекта
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Добавляем настройки для работы Приложения User
AUTH_USER_MODEL = "users.User"

# Данная настройка требуется для работы кастомной команды create_superuser, чтобы при переходе на страницу
# был переход к форме Входа
LOGIN_REDIRECT_URL = "/"
# Для Выхода, переадресует на Главную страницу
LOGOUT_REDIRECT_URL = "/"

# Настройки для отправки писем на почту сервиса Яндекс
EMAIL_HOST = "smtp.yandex.ru"
EMAIL_PORT = 465
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
# Пишем нашу почту, ту почту с которой будет отправляться письмо
# Получаем пароль для приложения следуя шагам на сайте https://yandex.ru/support/id/authorization/app-passwords.html
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
# Пишем пароль для Приложения Яндекс, а не пароль входа на Почту
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

# Дополнительные настройки для всех почтовых сервисов
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Настройка кеша для проекта в Django

# Флаг, который отвечает за глобальное состояние работоспособности кеша
CACHE_ENABLED = True

# "BACKEND": — бэкенд для обработки кеша и работы с хранилищем.
# "LOCATION":  — месторасположение хранилища.
# Если КЭШ работает, то
if CACHE_ENABLED:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",  # Прописываем путь до RedisCache
            "LOCATION": os.getenv("REDIS_HOST"),  # Где лежит redis
            # "LOCATION": "redis://127.0.0.1:6379",
            # "TIMEOUT": 300  # Ручная регулировка времени жизни кеша в секундах, по умолчанию 300
        }
    }

# Подключение к брокеру может быть закрыто авторизацией,
# поэтому настройки могут меняться и строка Location может выглядеть следующим образом:
# redis://username:password@127.0.0.1:6379
