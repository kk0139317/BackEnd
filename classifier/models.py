# models.py
from django.db import models


class Prediction(models.Model):
    image = models.ImageField(upload_to='uploads/')
    prediction = models.CharField(max_length=100)
    confidence = models.FloatField()
    url = models.URLField(max_length=200)
    image_name = models.CharField(max_length=255, null=True, blank=True)
    original_width = models.IntegerField(null=True, blank=True)
    original_height = models.IntegerField(null=True, blank=True)
    model_width = models.IntegerField(null=True, blank=True)
    model_height = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Prediction for {self.image} at {self.timestamp}"
