# Generated by Django 4.2.2 on 2023-09-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='time',
            field=models.CharField(default='09/19/2023 10:38:37 AM', max_length=50),
        ),
    ]