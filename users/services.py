# services.py
# This module contains business logic services such as prediction and recommendation engines.

from .models import Appliance, EnergyConsumption, Prediction
from django.utils import timezone
from datetime import timedelta

def generate_dummy_prediction(user_profile):
    """
    Generate dummy predictions for all appliances of the user for the next day.
    This is a stub function to simulate prediction logic.
    """
    from datetime import date
    next_day = date.today() + timedelta(days=1)
    appliances = Appliance.objects.filter(user_profile=user_profile)
    predictions = []
    for appliance in appliances:
        # Simple dummy prediction: average consumption of last 7 days or fixed value
        recent_consumptions = EnergyConsumption.objects.filter(appliance=appliance).order_by('-date')[:7]
        if recent_consumptions:
            avg_consumption = sum(c.consumption_kwh for c in recent_consumptions) / len(recent_consumptions)
        else:
            avg_consumption = 1.0  # default dummy value
        prediction = Prediction(
            user_profile=user_profile,
            appliance=appliance,
            predicted_date=next_day,
            predicted_consumption_kwh=avg_consumption
        )
        prediction.save()
        predictions.append(prediction)
    return predictions
