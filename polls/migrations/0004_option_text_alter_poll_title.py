# Generated by Django 4.1 on 2022-09-03 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_option_remove_poll_question_options_poll_author_vote_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
