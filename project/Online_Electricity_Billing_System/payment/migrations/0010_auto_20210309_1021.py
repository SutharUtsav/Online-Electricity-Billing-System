# Generated by Django 3.1.5 on 2021-03-09 04:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0009_auto_20210309_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netbanking',
            name='bank_name',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Invalid Bank Name', regex='^[atozAtoZ ]$')]),
        ),
    ]