# Generated by Django 4.2.5 on 2023-09-19 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tweets', '0002_alter_tweets_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='time',
            field=models.CharField(default='09/19/2023 03:46:23 PM', max_length=50),
        ),
    ]