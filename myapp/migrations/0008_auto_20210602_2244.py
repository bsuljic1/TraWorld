# Generated by Django 3.1.7 on 2021-06-02 20:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20210602_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocjena',
            name='vrijednost',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
