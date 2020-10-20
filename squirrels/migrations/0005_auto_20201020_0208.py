# Generated by Django 3.1.2 on 2020-10-20 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrels', '0004_auto_20201016_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='squirrel',
            name='Chasing',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='', help_text='If Squirrel Chasing', max_length=15),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Climbing',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='', help_text='If Squirrel Climbing', max_length=15),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Eating',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='', help_text='If Squirrel Eating', max_length=15),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Foraging',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='', help_text='If Squirrel Foraging', max_length=15),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='Running',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='', help_text='If Squirrel Running', max_length=15),
        ),
    ]
