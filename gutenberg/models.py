import datetime
from django.db import models


class eText(models.Model):
    """
    Trivial model representing a Project Gutenberg etext
    """

    rdf_id = models.CharField(unique=True, max_length=50)

    publisher = models.CharField(blank=True, max_length=100)
    title = models.CharField(blank=False, max_length=200)
    creator = models.TextField(blank=True)
    language = models.CharField(blank=False, max_length=100)
    created = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "eText"

    def __unicode__(self):
        return u"%s (%s)" % (self.title, self.rdf_id)
