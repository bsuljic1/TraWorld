# Generated by Django 3.1.7 on 2021-06-06 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20210607_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='recenzija',
            name='datum',
            field=models.DateField(auto_now=True),
        ),
    ]
