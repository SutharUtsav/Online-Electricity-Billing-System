# Generated by Django 3.1.5 on 2021-03-09 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0010_auto_20210309_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilebanking',
            name='ssn',
            field=models.CharField(max_length=9),
        ),
    ]
