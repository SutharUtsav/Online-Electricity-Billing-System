# Generated by Django 3.1.5 on 2021-03-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20210308_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cradit',
            name='bill_no',
            field=models.IntegerField(),
        ),
    ]
