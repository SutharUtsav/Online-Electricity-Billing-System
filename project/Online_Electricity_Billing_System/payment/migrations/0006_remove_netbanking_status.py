# Generated by Django 3.1.5 on 2021-03-08 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_netbanking_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='netbanking',
            name='status',
        ),
    ]