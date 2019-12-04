from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

from .models import Squirrel
from .forms import SquirrelForm

import datetime

def main_list(request):
    all_squirrels = Squirrel.objects.all()[::-1]
    return render(request, 'squirrel/main_list.html',{'all_squirrels':all_squirrels})
    
def add(request):
    context={}
    if request.method == 'POST':
            s = Squirrel()
            s.longitude = request.POST.get('longitude')
            s.latitude = request.POST.get('latitude')
            s.unique_squirrel_id = request.POST.get('unique_squirrel_id')
            s.shift = request.POST.get('shift')
            s.date = datetime.datetime.strptime(request.POST.get('date'),'%Y-%m-%d')
            date_error = None
            if s.date > datetime.datetime.now():
                date_error = 'Date automatically corrected to today!'
                s.date = datetime.datetime.now().date()
            s.age = request.POST.get('age')
            s.primary_fur_color = request.POST.get('primary_fur_color')
            s.location = request.POST.get('location')
            s.specific_location = request.POST.get('specific_location')
            s.running = request.POST.get('running')
            s.chasing = request.POST.get('chasing')
            s.climbing = request.POST.get('climbing')
            s.eating = request.POST.get('eating')
            s.foraging = request.POST.get('foraging')
            s.other_activities = request.POST.get('other_activities')
            s.kuks = request.POST.get('kuks')
            s.quaas = request.POST.get('quaas')
            s.moans = request.POST.get('moans')
            s.tail_flags = request.POST.get('tail_flags')
            s.tail_twitches = request.POST.get('tail_twitches')
            s.approaches = request.POST.get('approaches')
            s.indifferent = request.POST.get('indifferent')
            s.runs_from = request.POST.get('runs_from')
            s.save()
            success = 'Successfully added!'
            
            context = {'date_error':date_error,
                       'success':success,}
    return render(request,'squirrel/add.html',context)


def update_delete(request,unique_squirrel_id):
    instance = get_object_or_404(Squirrel, unique_squirrel_id=unique_squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST or None, instance=instance,auto_id=False)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            success = "Successfully Updated!"
            context = {'form': form,
                      'instance': instance,
                      'success': success,}

            return render(request, 'squirrel/edit.html', context)
    
        else:
            context= {'form': form,
                      'error': 'The form was not updated successfully.'}

            return render(request,'squirrel/edit.html' , context)      

    else:
        form = SquirrelForm(instance=instance,auto_id=False)
        context = {'form': form,
                  'instance': instance}

        return render(request, 'squirrel/edit.html', context)


def stats(request):
    from collections import Counter
    # number of adults per juvenile
    age_list = [value[0] for value in list(Squirrel.objects.all().values_list('age'))]
    age_dict = dict(Counter(age_list))
    adult_juvenile = age_dict['Adult']/age_dict['Juvenile']
    adult_juvenile = round(adult_juvenile,2)
    
    # fur color
    color_list = [value[0] for value in list(Squirrel.objects.all().values_list('primary_fur_color'))]
    color_dict = dict(Counter(color_list))
    color_dict.pop('')

    # shift
    shift_list = [value[0] for value in list(Squirrel.objects.all().values_list('shift'))]
    shift_dict = dict(Counter(shift_list))

    # response
    approaches_count = len([value[0] for value in list(Squirrel.objects.all().values_list('approaches')) if value[0] == 'true'])
    indifferent_count = len([value[0] for value in list(Squirrel.objects.all().values_list('indifferent')) if value[0] == 'true'])
    runs_from_count = len([value[0] for value in list(Squirrel.objects.all().values_list('runs_from')) if value[0] == 'true'])
    response_dict = {'Approaches':approaches_count,
            'Indifferent':indifferent_count,
            'Runs From': runs_from_count,}

    # tails
    tail_flag_count = len([value[0] for value in list(Squirrel.objects.all().values_list('tail_flags')) if value[0] == 'true'])
    tail_twitch_count = len([value[0] for value in list(Squirrel.objects.all().values_list('tail_twitches')) if value[0] == 'true'])
    tail_dict = {'Flags':tail_flag_count,
                     'Twitches':tail_twitch_count,}
    
    context = {'adult_juvenile': adult_juvenile,
               'color_dict': color_dict,
               'shift_dict': shift_dict,
               'response_dict': response_dict,
               'tail_dict':tail_dict,}
   
    return render(request,'squirrel/stats.html',context)


def map_plot(request):
    lats = Squirrel.objects.values_list('latitude',flat=True)
    longs = Squirrel.objects.values_list('longitude',flat=True)
    ids = Squirrel.objects.values_list('unique_squirrel_id',flat=True)

    geo_json = [ {"type": "Feature",
                        "properties": {
                            "id":  ident,
                            "popupContent":  "squirrel_id=%s" % (ident,) 
                            },
                        "geometry": {
                            "type": "Point",
                            "coordinates": [float(lon),float(lat)] }}
                        for ident,lon,lat in zip(ids,longs,lats) ] 
    context = {'geo_json':geo_json}

    return render(request, 'squirrel/map.html', context)

def delete(request,unique_squirrel_id):
    instance = get_object_or_404(Squirrel, unique_squirrel_id=unique_squirrel_id)
    if request.method == 'POST':
        instance.delete()

        return redirect('/sightings/')

    context = {'instance':instance}

    return render(request, 'squirrel/delete.html', context)
