# Generated by Django 3.1.5 on 2021-03-08 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_auto_20210309_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bhimupi',
            name='customer_no',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cradit',
            name='customer_no',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='mobilebanking',
            name='customer_no',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='netbanking',
            name='customer_no',
            field=models.CharField(max_length=255),
        ),
    ]