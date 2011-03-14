import os

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))

DATABASES = {"default": {"ENGINE": 'sqlite3',
                            "NAME": os.path.join(PROJECT_ROOT,
                                                    'haystack_bench.db')}}

INSTALLED_APPS = ('django.contrib.contenttypes', 'django.contrib.sites',
                    'haystack', 'gutenberg')

ROOT_URLCONF = 'bench_project.urls'

TEMPLATE_DIRS = os.path.join(os.path.dirname(__file__), "templates")

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

HAYSTACK_SITECONF = 'bench_project.search_sites'
HAYSTACK_SEARCH_ENGINE = 'whoosh'

HAYSTACK_INCLUDE_SPELLING = True

# HAYSTACK_SEARCH_ENGINE = 'solr'
# HAYSTACK_SOLR_URL = 'http://localhost:9001/solr/example'
# HAYSTACK_SOLR_TIMEOUT = 60 * 5

# For Whoosh:
import os
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = os.path.join(os.path.dirname(__file__), 'whoosh_index')
