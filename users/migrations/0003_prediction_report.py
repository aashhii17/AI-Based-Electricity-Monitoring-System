# Generated by Django 5.2 on 2025-05-11 16:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_appliance_energyconsumption'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predicted_date', models.DateField()),
                ('predicted_consumption_kwh', models.FloatField(help_text='Predicted energy consumption in kWh')),
                ('appliance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predictions', to='users.appliance')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predictions', to='users.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateField()),
                ('total_consumption_kwh', models.FloatField()),
                ('total_cost', models.FloatField()),
                ('efficiency', models.FloatField(help_text='Efficiency percentage')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='users.userprofile')),
            ],
        ),
    ]
