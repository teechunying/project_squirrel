from django import forms

from .models import Squirrel

class SquirrelForm(forms.ModelForm):

    class Meta:
        model = Squirrel
        fields = ('latitude','longitude','shift','date','age','primary_fur_color',
                  'location','specific_location','running',
                  'chasing','climbing','eating','foraging','other_activities',
                  'kuks','quaas','moans','tail_flags','tail_twitches','approaches',
                  'indifferent','runs_from',)

