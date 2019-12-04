from django.db import models
from django.utils.translation import gettext as _
import datetime
from django.utils import timezone
class Squirrel(models.Model):
    
    latitude = models.DecimalField(
        help_text =_('Latitude'),
        max_digits = 20,
        decimal_places = 15,
    )
    
    longitude = models.DecimalField(
        help_text =_('Longitude'),
        max_digits = 20,
        decimal_places = 15,
    )
    
    unique_squirrel_id = models.CharField(
        help_text = _('Unique Squirrel ID'),
        max_length = 50,
    )
    
    AM = 'AM'
    PM = 'PM'
    
    SHIFT_CHOICES = (
        (AM, 'AM'),
        (PM, 'PM'),
    )
    
    shift = models.CharField(
        help_text=_('Shift'),
        max_length=3,
        choices=SHIFT_CHOICES,
    )


    date = models.DateField(
        help_text=_('Date'),
        default=timezone.now,
   )


    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
    )

    age = models.CharField(
        help_text=_('Age'),
        max_length=10,
        choices=AGE_CHOICES,
    )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    COLOR_CHOICES = (
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
        (BLACK, 'Black')
    )

    primary_fur_color = models.CharField(
        help_text=_('Primary Fur Color'),
        max_length=10,
        choices=COLOR_CHOICES,
    )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'

    LOCATION_CHOICES = (
        (GROUND_PLANE, 'Ground Plane'),
        (ABOVE_GROUND, 'Above Ground'),
    )

    location = models.CharField(
        help_text=_('Location'),
        max_length=20,
        choices=LOCATION_CHOICES,
    )

    specific_location = models.CharField(
        help_text=_('Specific Location'),
        max_length=100,
        null=True,blank=True,
    )

    TRUE = 'true'
    FALSE = 'false'

    BINARY_CHOICES = (
        (TRUE, 'True'),
        (FALSE, 'False'),
    )

    running = models.CharField(
        help_text=_('Running'),
        max_length=15,
        choices=BINARY_CHOICES,
    )

    chasing = models.CharField(
        help_text=_('Chasing'),
        max_length=15,
        choices=BINARY_CHOICES,
    )

    climbing = models.CharField(
        help_text=_('Climbing'),
        max_length=15,
        choices=BINARY_CHOICES,
    )

    eating = models.CharField(
        help_text=_('Eating'),
        max_length=15,
        choices=BINARY_CHOICES,
    )

    foraging = models.CharField(
        help_text=_('Foraging'),
        max_length=15,
        choices=BINARY_CHOICES,
    )

    other_activities = models.CharField(
        help_text=_('Other Activities'),
        max_length=100,
        null=True, blank=True,
    )

    kuks = models.CharField(
        help_text=_('Kuks'),
        max_length=15,
        choices=BINARY_CHOICES,
    )

    quaas = models.CharField(
        help_text=_('Quaas'),
        max_length=15,
        choices=BINARY_CHOICES,
    )

    moans = models.CharField(
        help_text=_('Moans'),
        max_length=15,
        choices=BINARY_CHOICES,
    )

    tail_flags = models.CharField(
        help_text=_('Tail Flags'),
        max_length=15,
        choices=BINARY_CHOICES,
    )

    tail_twitches = models.CharField(
        help_text=_('Tail Twitches'),
        max_length=15,
        choices=BINARY_CHOICES,
    )

    approaches = models.CharField(
        help_text=_('Approaches'),
        max_length=15,
        choices=BINARY_CHOICES,
    )

    indifferent = models.CharField(
        help_text=_('Indifferent'),
        max_length=15,
        choices=BINARY_CHOICES,
    )

    runs_from = models.CharField(
        help_text=_('Runs From'),
        max_length=15,
        choices=BINARY_CHOICES,
    )

    def __str__(self):
        return self.unique_squirrel_id

# Create your models here.
