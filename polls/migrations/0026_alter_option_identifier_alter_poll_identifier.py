# Generated by Django 4.1 on 2022-09-05 12:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0025_alter_option_identifier_alter_poll_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('b1c0fbbc-4c92-4ab3-8777-f0c894f161cf'), null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('68905987-d17f-41df-a326-0c7d40c8fc87'), null=True),
        ),
    ]
