from haystack.indexes import SearchIndex, CharField, DateField
from haystack import site

from .models import eText


class eTextIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    publisher = CharField(model_attr='publisher', faceted=True)
    creator = CharField(model_attr='creator', null=True, faceted=True)
    title = CharField(model_attr='title')
    created = DateField(model_attr='created', null=True, faceted=True)


site.register(eText, eTextIndex)
