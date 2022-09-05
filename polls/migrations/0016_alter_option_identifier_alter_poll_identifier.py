# Generated by Django 4.1 on 2022-09-05 07:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_alter_option_identifier_alter_poll_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('ee10fa16-2f03-4a06-a668-0938ddd267b2'), null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('31642f75-791c-4a50-88e0-1a901faf8692'), null=True),
        ),
    ]
