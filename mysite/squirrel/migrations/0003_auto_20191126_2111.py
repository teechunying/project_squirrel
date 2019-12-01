# Generated by Django 2.2.7 on 2019-11-27 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0002_auto_20191126_2028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='squirrel',
            old_name='approahces',
            new_name='approaches',
        ),
        migrations.RenameField(
            model_name='squirrel',
            old_name='other_activites',
            new_name='other_activities',
        ),
        migrations.AddField(
            model_name='squirrel',
            name='location',
            field=models.CharField(choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], default='Ground Plane', help_text='Location', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='age',
            field=models.CharField(choices=[('adult', 'Adult'), ('juvenile', 'Juvenile')], default='adult', help_text='Age', max_length=10),
        ),
    ]
