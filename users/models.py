from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20, unique=True)
    physical_address = models.TextField()

    def __str__(self):
        return self.full_name

class Appliance(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='appliances')
    name = models.CharField(max_length=255)
    power_rating = models.FloatField(help_text="Power rating in watts")
    quantity = models.PositiveIntegerField(default=1)
    days_used_per_week = models.PositiveIntegerField(default=7, help_text="Number of days appliance is used per week")
    usage_time = models.FloatField(default=1.0, help_text="Daily usage time in hours")

    def __str__(self):
        return f"{self.name} ({self.quantity})"

class EnergyConsumption(models.Model):
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE, related_name='consumptions')
    date = models.DateField()
    consumption_kwh = models.FloatField(help_text="Energy consumption in kWh")

    def __str__(self):
        return f"{self.appliance.name} - {self.date} : {self.consumption_kwh} kWh"

class Prediction(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='predictions')
    appliance = models.ForeignKey(Appliance, on_delete=models.CASCADE, related_name='predictions')
    predicted_date = models.DateField()
    predicted_consumption_kwh = models.FloatField(help_text="Predicted energy consumption in kWh")

    def __str__(self):
        return f"Prediction for {self.appliance.name} on {self.predicted_date}: {self.predicted_consumption_kwh} kWh"

class Report(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reports')
    report_date = models.DateField()
    total_consumption_kwh = models.FloatField()
    total_cost = models.FloatField()
    efficiency = models.FloatField(help_text="Efficiency percentage")

    def __str__(self):
        return f"Report for {self.user_profile.full_name} on {self.report_date}"
