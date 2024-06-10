# serializers.py
from rest_framework import serializers
from .models import Prediction
from django.contrib.auth.models import User
class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = [  
                    'id',
                    'image',
                    'prediction',
                    'confidence',
                    'timestamp', 
                    'url', 
                    'image_name', 
                    'original_width', 
                    'original_height', 
                    'model_width', 
                    'model_height' 
                    ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password'] 