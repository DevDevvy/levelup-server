# Generated by Django 4.0.4 on 2022-05-02 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_rename_type_game_type_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='gamers', to='levelupapi.gamer'),
        ),
    ]
