# Generated by Django 4.1 on 2022-09-05 08:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_remove_poll_options_alter_option_identifier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('268e43e4-6531-4f40-ae69-da10badc2977'), null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('f614acbe-d1b6-435f-a2d6-6f88de0ec160'), null=True),
        ),
    ]
