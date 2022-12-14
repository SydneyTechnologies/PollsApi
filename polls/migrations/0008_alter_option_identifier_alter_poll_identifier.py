# Generated by Django 4.1 on 2022-09-05 06:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_option_identifier_alter_poll_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('0e77b690-c6f4-48e5-8e90-e1d023859d2b'), null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('4c16e5bd-f5ab-4f4b-bfc8-29158c8f5b48'), null=True),
        ),
    ]
