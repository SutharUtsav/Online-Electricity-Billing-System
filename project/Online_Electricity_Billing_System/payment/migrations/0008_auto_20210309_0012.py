# Generated by Django 3.1.5 on 2021-03-08 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_auto_20210309_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilebanking',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=17),
        ),
    ]