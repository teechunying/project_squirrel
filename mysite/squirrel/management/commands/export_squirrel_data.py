from django.core.management.base import BaseCommand, CommandError
import os
import csv

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('csvfile', nargs='+',type=str)

    def handle(self, *args, **options):
        path = options['csvfile'][0]
        from squirrel.models import Squirrel
        import datetime
        with open(path, 'w', newline='') as csvFile:
            varlist = [v for v in vars(Squirrel.objects.all()[0]).keys() if v not in ['_state', 'id']]
            writer = csv.writer(csvFile, delimiter=',')
            writer.writerow([Squirrel._meta.get_field(v).help_text for v in varlist])
            for instance in Squirrel.objects.all():
                writer.writerow([getattr(instance, v) for v in varlist])

