import numpy as np
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

# Load the pre-trained VGG16 model + higher level layers
model = VGG16(weights='imagenet')

def classify_image(img_path):
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Predict
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=1)[0]

    return {
        'prediction': decoded_predictions[0][1],
        'confidence': float(decoded_predictions[0][2]) * 100
    }
