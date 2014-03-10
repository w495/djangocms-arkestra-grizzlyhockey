# -*- coding: utf-8 -*-
# Django settings for project project.

import os.path

# Make it work straight from the checkout!
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

# set the BASE_PATH for convenience's sake
BASE_PATH = os.path.normpath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@project.com'),
)


import os
import sys
import logging
import platform


import os
import django
from time import gmtime, strftime

PATH = os.path.abspath(os.path.dirname(__file__))

NODENAME="%s_%s_%s_%s"%(
    platform.node().replace('.', '_').replace('-', '_'),
    django.get_version(),
    platform.python_implementation(),
    platform.python_version()
)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ghl',                      # Or path to database file if using sqlite3.
        'USER': 'monty',                      # Not used with sqlite3.
        'PASSWORD': 'some_pass',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'
DATE_FORMAT = "jS F Y"
TIME_FORMAT = "H\.i"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = BASE_PATH+'/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://project.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_PATH, "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'legacy_finders.LegacyAppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+l!v($pn27-@l_7=9&amp;r-^wl!cqyn=yi3npu9dv02@c@th-or7n'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    'django.core.context_processors.static',
    # 'django.core.context_processors.csrf',
    'django.contrib.messages.context_processors.messages',

    "cms.context_processors.media",
    'sekizai.context_processors.sekizai',

    "arkestra_utilities.context_processors.arkestra_templates",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',

    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    BASE_PATH+'/templates/',
)

INSTALLED_APPS = (

     # Django CMS applications

    'arkestra_utilities',
    'cms',
    'menus',
    # 'appmedia',
    'cms.plugins.text',
    'cms.plugins.snippet',
    'sekizai',
    # 'djcelery',     # will need to be enabled for celery processing

    # Arkestra applications

    'contacts_and_people',
    'vacancies_and_studentships',
    'news_and_events',
    'links',
    'arkestra_utilities.widgets.combobox',
    'arkestra_image_plugin',
    'video',
    'housekeeping',
    'polls',

    'grizzly',

    # other applications


    'cmsplugin_bootstrap_carousel',
    'polymorphic',
    'semanticeditor',
    'mptt',
    'easy_thumbnails',
    'typogrify',
    'filer',
    'widgetry',
    'south', # don't leave this disabled
    'treeadmin',
    'pagination',

    # core Django applications
    # these should be last, so we can override their templates

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'django.contrib.markup'
)

BOOTSTRAP_CAROUSEL_IMGSIZE = (10000, 300)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.




if not ('LOGDIRTIME' in vars()):
    #LOGDIRTIME = strftime("%Y-%m-%d/%H-%M-%S", gmtime())
    LOGDIRTIME = strftime("%Y-%m-%d", gmtime())

LOGDIR =  "/var/log/pybsadm/%s/%s" % (NODENAME, LOGDIRTIME)

#if DEBUG:

LOGDIR =  "priv/logs/%s/%s" % (NODENAME, LOGDIRTIME)

if not os.path.exists(LOGDIR):
    os.makedirs(LOGDIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'pybsadm_formater': {
            'format':   '%(asctime)s %(levelname)s <%(process)d> '
                        '%(message)s '
            #'format':   '%(levelname)s [%(asctime)s ] \n'
                        #'*  logger   = %(name)s \n'
                        #'*  file     = %(filename)s \n'
                        #'*           = %(pathname)s \n'
                        #'*  line     = %(lineno)d \n'
                        #'*  module   = %(module)s \n'
                        #'*  function = %(funcName)s \n'
                        #'*  process  = %(process)d \n'
                        #'*           = %(processName)s \n'
                        #'*  thread   = %(thread)s \n'
                        #'*           = %(threadName)s \n'
                        #'*  message = \n\n'
                        #'%(message)s \n\n'
                        #'*  exc_info = \n\n'
                        #'%(exc_info)s \n\n',
            #'datefmt': "%Y_%m_%d %H:%M:%S",
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },

        'console':{
            'level': 'DEBUG',

            'class': 'logging.StreamHandler',
            'formatter': 'pybsadm_formater',
        },

        #'production_critical_logfile':{
            #'level' : 'CRITICAL',
            #'class' : 'logging.handlers.TimedRotatingFileHandler',
            #'filename' : '%s/production.critical.log' % LOGDIR,
            #'when' : 'midnight',
            #'interval' :    1,
            #'backupCount' : 7,
            #'formatter': 'pybsadm_formater',
            #'filters': ['require_debug_false'],
        #},

        #'production_error_logfile':{
            #'level' : 'ERROR',
            #'class' : 'logging.handlers.TimedRotatingFileHandler',
            #'filename' : '%s/production.error.log' % LOGDIR,
            #'when' : 'midnight',
            #'interval' :    1,
            #'backupCount' : 7,
            #'formatter': 'pybsadm_formater',
            #'filters': ['require_debug_false'],
        #},

        #'production_warning_logfile':{
            #'level' : 'WARNING',
            #'class' : 'logging.handlers.TimedRotatingFileHandler',
            #'filename' : '%s/production.warning.log' % LOGDIR,
            #'when' : 'midnight',
            #'interval' :    1,
            #'backupCount' : 7,
            #'formatter': 'pybsadm_formater',
            #'filters': ['require_debug_false'],
        #},

        #'production_info_logfile':{
            #'level' : 'INFO',
            #'class' : 'logging.handlers.TimedRotatingFileHandler',
            #'filename' : '%s/production.info.log' % LOGDIR,
            #'when' : 'midnight',
            #'interval' :    1,
            #'backupCount' : 7,
            #'formatter': 'pybsadm_formater',
            #'filters': ['require_debug_false'],
        #},


        'development_critical_logfile':{
            'level' : 'CRITICAL',
            'class' : 'logging.handlers.TimedRotatingFileHandler',
            'filename' : '%s/development.critical.log' % LOGDIR,
            'when' : 'midnight',
            'interval' :    1,
            'backupCount' : 7,
            'formatter': 'pybsadm_formater',
        },

        'development_error_logfile':{
            'level' : 'ERROR',
            'class' : 'logging.handlers.TimedRotatingFileHandler',
            'filename' : '%s/development.error.log' % LOGDIR,
            'when' : 'midnight',
            'interval' :    1,
            'backupCount' : 7,
            'formatter': 'pybsadm_formater',

        },

        'development_warning_logfile':{
            'level' : 'WARNING',
            'class' : 'logging.handlers.TimedRotatingFileHandler',
            'filename' : '%s/development.warning.log' % LOGDIR,
            'when' : 'midnight',
            'interval' :    1,
            'backupCount' : 7,
            'formatter': 'pybsadm_formater',

        },

        'development_info_logfile':{
            'level' : 'INFO',
            'class' : 'logging.handlers.TimedRotatingFileHandler',
            'filename' : '%s/development.info.log' % LOGDIR,
            'when' : 'midnight',
            'interval' :    1,
            'backupCount' : 7,
            'formatter': 'pybsadm_formater',

        },

        'development_degug_logfile':{
            'level' : 'DEBUG',
            'class' : 'logging.handlers.TimedRotatingFileHandler',
            'filename' : '%s/development.degug.log' % LOGDIR,
            'when' : 'midnight',
            'interval' :    1,
            'backupCount' : 7,
            'formatter': 'pybsadm_formater',

        },

        'django_debug_logfile':{
            'level' : 'DEBUG',
            'class' : 'logging.handlers.TimedRotatingFileHandler',
            'filename' : '%s/django.debug.log' % LOGDIR,
            'when' : 'midnight',
            'interval' :    1,
            'backupCount' : 7,
            'formatter': 'pybsadm_formater',

        },

        'database_debug_logfile':{
            'level' : 'DEBUG',
            'class' : 'logging.handlers.TimedRotatingFileHandler',
            'filename' : '%s/database.debug.log' % LOGDIR,
            'when' : 'midnight',
            'interval' :    1,
            'backupCount' : 7,
            'formatter': 'pybsadm_formater',

        },

        'py_warning_logfile':{
            'level' : 'WARNING',
            'class' : 'logging.handlers.TimedRotatingFileHandler',
            'filename' : '%s/py.warning.log' % LOGDIR,
            'when' : 'midnight',
            'interval' :    1,
            'backupCount' : 7,
            'formatter': 'pybsadm_formater',

        },

        'request_debug_logfile':{
            'level' : 'DEBUG',
            'class' : 'logging.handlers.TimedRotatingFileHandler',
            'filename' : '%s/request.debug.log' % LOGDIR,
            'when' : 'midnight',
            'interval' :    1,
            'backupCount' : 7,
            'formatter': 'pybsadm_formater',

        },

        'project_info_logfile':{
            'level' : 'DEBUG',
            'class' : 'logging.handlers.TimedRotatingFileHandler',
            'filename' : '%s/project.info.log' % LOGDIR,
            'when' : 'midnight',
            'interval' :    1,
            'backupCount' : 7,
            'formatter': 'pybsadm_formater'
        },



        'null': {
            "class": 'django.utils.log.NullHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': [
                'mail_admins',
                'console',
                'request_debug_logfile'
            ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers': [
                'django_debug_logfile',
            ],
            'level': "DEBUG",
        },
        'django.db.backends':{
            'handlers': [
                'database_debug_logfile'
            ],
            'level': "DEBUG",
        },
        'py.warnings': {
            'handlers': [
                'py_warning_logfile'
            ],
            'level': "DEBUG",
        },
        'project': {
            'handlers': [
                'project_info_logfile'
            ],
            'level': "INFO",
        },
        '': {
            'handlers': [
                'console',
                #'production_critical_logfile',
                #'production_error_logfile',
                #'production_warning_logfile',
                #'production_info_logfile',
                'development_critical_logfile',
                'development_error_logfile',
                'development_warning_logfile',
                'development_info_logfile',
                'development_degug_logfile',
            ],
            'level': "DEBUG",
        },
    }
}


THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    )

# ------------------------ Django Celery
try:
    import djcelery
    djcelery.setup_loader()

    BROKER_HOST = "localhost"
    BROKER_PORT = 5672
    BROKER_USER = "guest"
    BROKER_PASSWORD = "guest"
    BROKER_VHOST = "/"
except ImportError:
    pass


# ------------------------ Django Filer

FILER_FILE_MODELS = (
        'video.models.Video',
        'filer.models.imagemodels.Image',
        'filer.models.filemodels.File',
    )

# ------------------------ Django CMS

gettext = lambda s: s

CMS_SOFTROOT = True
CMS_PERMISSION = True
CMS_SEO_FIELDS = True


# this is only here because I don't know how to make other apps find it otherwise, and they rely on it.
CMS_MEDIA_URL = STATIC_URL + 'cms/'

CMS_TEMPLATES = (
    ('base.html', gettext('base')),
    ('title.html', gettext('title')),
)

CMS_PAGE_FLAGS = (
    ('no_local_menu', 'Hide local menu') ,
    ('no_horizontal_menu', 'No horizontal menu') ,
    ('no_page_title', "Don't display page title") ,
    )

CMS_PLACEHOLDER_CONF = {
    'body': {
        # "plugins": (
        #     'SemanticTextPlugin',
        #     'CMSVacanciesPlugin',
        #     'CMSNewsAndEventsPlugin',
        #     'SnippetPlugin',
        #     'LinksPlugin',
        #     'CMSPublicationsPlugin',
        #     'ImagePlugin',
        #     'ImageSetPublisher',
        #     'EntityAutoPageLinkPluginPublisher',
        #     'EntityMembersPluginPublisher',
        #     'FilerImagePlugin',
        #     'EntityDirectoryPluginPublisher',
        #     'CarouselPluginPublisher',
        #     'FocusOnPluginPublisher',
        #     'VideoPluginPublisher',
        #     ),
        "extra_context": {
            "width":"880",
            },
        "name": gettext("body"),
    },
}

LANGUAGES = (
    ('en', gettext('English')),
    ('ru', gettext('Russian'))
)

# ------------------------ WYMeditor/SemanticEditor

# these override the settings in cms.plugins.text.settings

WYM_TOOLS = ",\n".join([
    "{'name': 'Italic', 'title': 'Emphasis', 'css': 'wym_tools_emphasis'}",
    "{'name': 'Bold', 'title': 'Strong', 'css': 'wym_tools_strong'}",
    "{'name': 'InsertOrderedList', 'title': 'Ordered_List', 'css': 'wym_tools_ordered_list'}",
    "{'name': 'InsertUnorderedList', 'title': 'Unordered_List', 'css': 'wym_tools_unordered_list'}",
    "{'name': 'Indent', 'title': 'Indent', 'css': 'wym_tools_indent'}",
    "{'name': 'Outdent', 'title': 'Outdent', 'css': 'wym_tools_outdent'}",
    "{'name': 'Undo', 'title': 'Undo', 'css': 'wym_tools_undo'}",
    "{'name': 'Redo', 'title': 'Redo', 'css': 'wym_tools_redo'}",
    "{'name': 'ToggleHtml', 'title': 'HTML', 'css': 'wym_tools_html'}",
])

WYM_CONTAINERS = ",\n".join([
    "{'name': 'P', 'title': 'Paragraph', 'css': 'wym_containers_p'}",
   # "{'name': 'H1', 'title': 'Heading_1', 'css': 'wym_containers_h1'}", # I assume you reserve <h1> for your page templates
    "{'name': 'H2', 'title': 'Heading_2', 'css': 'wym_containers_h2'}",
    "{'name': 'H3', 'title': 'Heading_3', 'css': 'wym_containers_h3'}",
    "{'name': 'H4', 'title': 'Heading_4', 'css': 'wym_containers_h4'}",
    "{'name': 'H5', 'title': 'Heading_5', 'css': 'wym_containers_h5'}",
    "{'name': 'H6', 'title': 'Heading_6', 'css': 'wym_containers_h6'}",
#    "{'name': 'PRE', 'title': 'Preformatted', 'css': 'wym_containers_pre'}",
   "{'name': 'BLOCKQUOTE', 'title': 'Blockquote', 'css': 'wym_containers_blockquote'}",
   # "{'name': 'TH', 'title': 'Table_Header', 'css': 'wym_containers_th'}", # not ready for this yet
])

from arkestra_settings import *# import pdb; pdb.set_trace()
