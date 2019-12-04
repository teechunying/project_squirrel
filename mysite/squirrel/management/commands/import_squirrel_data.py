from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('csvfile',nargs='+',type=str)

    def handle(self, *args, **options):
        path = options['csvfile'][0]
        import os
        import csv
        from squirrel.models import Squirrel
        import datetime
        with open(path, 'r') as csvFile:
            reader = csv.DictReader(csvFile, delimiter=',')
            for row in reader:
                while row['Unique Squirrel ID'] in Squirrel.objects.values_list('unique_squirrel_id',flat=True):
                    row['Unique Squirrel ID'] += '-R'
                s=Squirrel(latitude=row['Y'],
                        longitude=row['X'],
                        unique_squirrel_id=row['Unique Squirrel ID'],
                        shift=row['Shift'],
                        date=datetime.datetime.strptime(row['Date'],'%m%d%Y'),
                        age=row['Age'],
                        primary_fur_color=row['Primary Fur Color'],
                        location=row['Location'],
                        specific_location=row['Specific Location'],
                        running=row['Running'],
                        chasing=row['Chasing'],
                        climbing=row['Climbing'],
                        eating=row['Eating'],
                        foraging=row['Foraging'],
                        other_activities=row['Other Activities'],
                        kuks=row['Kuks'],
                        quaas=row['Quaas'],
                        moans=row['Moans'],
                        tail_flags=row['Tail flags'],
                        tail_twitches=row['Tail twitches'],
                        approaches=row['Approaches'],
                        indifferent=row['Indifferent'],
                        runs_from=row['Runs from'])
                s.save()

            print('Imported ',len(Squirrel.objects.all()), 'squirrel sightings!')


        


