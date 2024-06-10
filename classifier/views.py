import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
# from .image_classifier import classify_image
from .cat_and_dog import predict_image
from django.conf import settings
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Prediction
from .serializers import *
import json
from PIL import Image

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_obj = request.data['file']
        media_dir = settings.MEDIA_ROOT
        if not os.path.exists(media_dir):
            os.makedirs(media_dir)
        
        img_path = os.path.join(media_dir, file_obj.name)
        with open(img_path, 'wb+') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
        
        # Classify the image
        result = predict_image(img_path)
        image = file_obj
        prediction = result['prediction']
        confidence = result['confidence']
        url = request.data['url']
        
        # Get image dimensions
        img = Image.open(img_path)
        original_width, original_height = img.size
        
        # Define model dimensions
        model_width, model_height = 224, 224  # Change as needed to match your model

        # Save to the database
        datasets = Prediction(
            image=image,
            prediction=prediction,
            confidence=confidence,
            url=url,
            image_name=file_obj.name,
            original_width=original_width,
            original_height=original_height,
            model_width=model_width,
            model_height=model_height
        )
        datasets.save()
        
        # Include additional data in the response
        result.update({
            'image_name': file_obj.name,
            'original_width': original_width,
            'original_height': original_height,
            'model_width': model_width,
            'model_height': model_height
        })
        
        return Response(result)

class PredictionList(APIView):
    def get(self, request):
        predictions = Prediction.objects.all().order_by('-timestamp')
        serializer = PredictionSerializer(predictions, many=True)
        return Response(serializer.data)


