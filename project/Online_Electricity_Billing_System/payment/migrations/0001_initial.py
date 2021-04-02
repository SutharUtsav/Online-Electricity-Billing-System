# Generated by Django 3.1.5 on 2021-03-07 17:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bhimUPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_no', models.CharField(max_length=255)),
                ('bill_no', models.CharField(max_length=20)),
                ('bill_amount', models.PositiveIntegerField()),
                ('upi_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='cradit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_no', models.CharField(max_length=255)),
                ('bill_no', models.CharField(max_length=20)),
                ('bill_amount', models.PositiveIntegerField()),
                ('card_number', models.PositiveIntegerField()),
                ('cvv', models.PositiveIntegerField()),
                ('expiry_date', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='mobilebanking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_no', models.CharField(max_length=255)),
                ('bill_no', models.CharField(max_length=20)),
                ('bill_amount', models.PositiveIntegerField()),
                ('mobile_no', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\d{9,15}$')])),
                ('ssn', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NetBanking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_no', models.CharField(max_length=255)),
                ('bill_no', models.CharField(max_length=20)),
                ('bill_amount', models.PositiveIntegerField()),
                ('bank_name', models.CharField(max_length=255)),
                ('branch_code', models.CharField(max_length=255)),
                ('account_no', models.CharField(max_length=255)),
            ],
        ),
    ]
