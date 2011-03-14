# encoding: utf-8

import os
import sys
from timeit import default_timer as clock
from contextlib import closing

from django.utils import simplejson as json
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.test.client import Client

from haystack.query import SearchQuerySet

from performance_tools.memory import Heap
from performance_tools.query_counts import QueryCounter

from gutenberg.models import eText


class Command(BaseCommand):
    args = 'path/to/results/dir'
    help = 'Run benchmarks and save the result to the provided directory'

    def handle(self, result_dir, *args, **kwargs):
        if not os.path.exists(result_dir):
            raise CommandError("You must provide the result directory")

        self.client = Client()

        for bench_f in ("rebuild_index", "trivial_search", "basic_faceting"):
            res = self.bench(getattr(self, bench_f))

            for k, v in res.items():
                bench_name = "%s-%s" % (bench_f, k)
                data = {"benchmark": bench_name, "result_value": float(v)}

                with closing(open(os.path.join(result_dir, "%s.json" % bench_name), "wb")) as f:
                    json.dump(data, f)

    def bench(self, f):
        queries = QueryCounter()
        heap = Heap()
        start_time = clock()

        f()

        elapsed = clock() - start_time
        return {
            "time": elapsed,
            "heap": heap.deltas()['size'],
            "queries": sum(queries.deltas().values())
        }

    def rebuild_index(self):
        call_command("rebuild_index", interactive=False, verbosity=0)

    def trivial_search(self):
        """Simple whole-path benchmark"""
        
        resp = self.client.get("/?q=america")
        if resp.status_code != 200:
            raise RuntimeError(u"Query failed: %s" % resp)

    def basic_faceting(self):
        # NOTE: Currently does nothing on Whoosh due to lack of backend support
        sqs = SearchQuerySet().filter(content="america")
        sqs = sqs.facet("publisher")
        fc = sqs.facet_counts()
