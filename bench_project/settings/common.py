import os

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))

DATABASES = {"default": {"ENGINE": 'sqlite3',
                            "NAME": os.path.join(PROJECT_ROOT,
                                                    'haystack_bench.db')}}

INSTALLED_APPS = ('django.contrib.contenttypes', 'django.contrib.sites',
                    'haystack', 'gutenberg')

ROOT_URLCONF = 'bench_project.urls'

TEMPLATE_DIRS = os.path.join(PROJECT_ROOT, "bench_project", "templates")

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

HAYSTACK_SITECONF = 'bench_project.search_sites'
HAYSTACK_INCLUDE_SPELLING = True
