# Generated by Django 4.1.2 on 2022-10-25 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0004_participants'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Participants',
            new_name='Participant',
        ),
        migrations.AddField(
            model_name='meetup',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, to='meetups.participant'),
        ),
    ]
