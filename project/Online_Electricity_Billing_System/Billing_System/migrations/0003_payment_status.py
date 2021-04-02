# Generated by Django 3.1.5 on 2021-03-09 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Billing_System', '0002_auto_20210308_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Billing_System.generate_bill', verbose_name='month')),
                ('key_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]