# Generated by Django 4.1 on 2022-09-05 12:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_alter_option_identifier_alter_poll_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('15c1cd04-8fbf-41c5-9bed-29e6e726e14f'), null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('229e037c-7b3f-4b09-b36c-8bd0bf09f339'), null=True),
        ),
    ]
