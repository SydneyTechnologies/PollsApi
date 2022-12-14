# Generated by Django 4.1 on 2022-09-05 12:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0023_alter_option_identifier_alter_poll_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('f62c92e5-a784-4799-8573-a24657ba3336'), null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='identifier',
            field=models.UUIDField(blank=True, default=uuid.UUID('92d5392d-27c2-4df4-93cc-08f7e50bf0df'), null=True),
        ),
    ]
