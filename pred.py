import tensorflow as tf
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the pre-trained VGG16 model + higher level layers
model = VGG16(weights='imagenet')

def classify_image(img_path):
    # Load the image and resize it to 224x224 pixels (required by VGG16)
    img = image.load_img(img_path, target_size=(224, 224))
    
    # Convert the image to a numpy array
    img_array = image.img_to_array(img)
    
    # Expand dimensions to match the shape required by the model
    img_array = np.expand_dims(img_array, axis=0)
    
    # Preprocess the image input for the VGG16 model
    img_array = preprocess_input(img_array)
    
    # Predict the class probabilities for the image
    predictions = model.predict(img_array)
    
    # Decode the predictions to class names
    decoded_predictions = decode_predictions(predictions, top=1)[0]
    
    return decoded_predictions

# Example usage:
img_path = 'Image.jpg'  # Replace with your image path
predictions = classify_image(img_path)

for pred in predictions:
    print(f"Predicted: {pred[1]} with confidence {pred[2]*100:.2f}%")
