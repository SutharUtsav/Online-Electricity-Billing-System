# Generated by Django 3.1.5 on 2021-03-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0011_auto_20210309_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cradit',
            name='expiry_date',
            field=models.DateField(),
        ),
    ]
