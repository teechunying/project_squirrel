from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self,*args,**options):
        from squirrel.models import Squirrel
        print('previous count:', len(Squirrel.objects.all()))
        Squirrel.objects.all().delete()
        print('new count:', len(Squirrel.objects.all()))
        
