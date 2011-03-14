# encoding: utf-8

import xml.sax
import sys

from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError

from gutenberg.models import eText


class Command(BaseCommand):
    args = 'path/to/catalog.rdf'
    help = 'Import a Gutenberg catalog RDF file'

    def handle(self, *args, **options):

        class eTextHandler(xml.sax.ContentHandler):
            eText = None
            content = None

            def startElement(self, name, attrs):
                self.content = u""

                if name == u"pgterms:etext":
                    self.eText, created = eText.objects.get_or_create(rdf_id=attrs['rdf:ID'])

            def characters(self, content):
                if not content.strip():
                    return

                if hasattr(self, "content"):
                    self.content += content

            def endElement(self, name):
                if name == u"pgterms:etext":
                    try:
                        self.eText.full_clean()
                        self.eText.save()
                    except ValidationError, e:
                        print >>sys.stderr, u"ERROR: %s failed validation: %s" % (self.eText, e)
                    self.eText = None
                else:
                    namespace, name = name.split(":", 1)
                    if hasattr(self.eText, name):
                        setattr(self.eText, name, self.content)


        parser = xml.sax.make_parser()
        parser.setContentHandler(eTextHandler())

        for filename in args:
            parser.parse(open(filename, "rb"))
