from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np
import json

# Load the saved model
model = load_model('model.h5')

# Image preprocessing function
def preprocess_image(img_path):
    WIDTH, HEIGHT = 224, 224  # Update to match the model's input shape
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(WIDTH, HEIGHT))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = img_array / 255.0  # Normalize
    return img_array.reshape((1, WIDTH, HEIGHT, 3))  # Add an extra dimension

# Prediction function
def predict_image(image_path):
    # Preprocess image
    class_names = ['cat', 'dog']
    new_image = preprocess_image(image_path)
    # Make prediction
    prediction = model.predict(new_image)
    # Decode prediction
    predicted_class = np.argmax(prediction[0])
    predicted_label = class_names[predicted_class]
    confidence_percentage = round(np.max(prediction[0]) * 100, 2)
    return {'prediction': predicted_label, 'confidence': confidence_percentage}

if __name__ == "__main__":
    # Specify the class names
    class_names = ['cat', 'dog']

    # Provide the image path
    image_path = 'Image.jpg'  # Replace with your image path

    # Perform prediction
    result = predict_image(image_path, class_names)

    # Output result in JSON format
    print(json.dumps(result, indent=4))
