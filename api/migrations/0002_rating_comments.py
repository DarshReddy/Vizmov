# Generated by Django 3.0.3 on 2020-02-24 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='comments',
            field=models.TextField(default='', max_length=256),
        ),
    ]
