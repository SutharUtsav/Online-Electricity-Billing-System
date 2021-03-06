# Generated by Django 3.1.5 on 2021-03-08 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Billing_System', '0001_initial'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bhimupi',
            name='bill_amount',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='bhimupi',
            name='bill_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Billing_System.generate_bill'),
        ),
        migrations.AlterField(
            model_name='cradit',
            name='bill_amount',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='cradit',
            name='bill_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Billing_System.generate_bill'),
        ),
        migrations.AlterField(
            model_name='mobilebanking',
            name='bill_amount',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='mobilebanking',
            name='bill_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Billing_System.generate_bill'),
        ),
        migrations.AlterField(
            model_name='netbanking',
            name='bill_amount',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='netbanking',
            name='bill_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Billing_System.generate_bill'),
        ),
    ]
