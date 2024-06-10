# serializers.py
from rest_framework import serializers
from .models import Prediction

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
