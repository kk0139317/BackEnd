# views.py

import base64
import io
import numpy as np
from PIL import Image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Load the pre-trained VGG16 model
model = VGG16(weights='imagenet')

@csrf_exempt
def classify_frame(request):
    if request.method == 'POST':
        image_data = request.POST.get('image', '')

        # Decode base64 image data and convert to PIL Image
        image_bytes = base64.b64decode(image_data.split(',')[1])
        image = Image.open(io.BytesIO(image_bytes))

        # Resize image to match VGG16 input size
        image = image.resize((224, 224))

        # Preprocess image
        img_array = np.expand_dims(image, axis=0)
        img_array = preprocess_input(img_array)

        # Predict
        predictions = model.predict(img_array)
        decoded_predictions = decode_predictions(predictions, top=1)[0]

        # Extract prediction class and confidence
        prediction = decoded_predictions[0][1]
        confidence = float(decoded_predictions[0][2]) * 100

        return JsonResponse({'prediction': prediction, 'confidence': confidence})
    else:
        return JsonResponse({'error': 'POST method required'})
