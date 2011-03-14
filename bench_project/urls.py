# -*- coding: utf-8 -*-

import os.path

from django.conf import settings
from django.conf.urls.defaults import url, patterns, include, handler404, handler500

urlpatterns = patterns('',
    (r'', include('haystack.urls')),
)
