import cv2
import numpy as np
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

# Load the pre-trained VGG16 model + higher level layers
model = VGG16(weights='imagenet')

def classify_frame(frame):
    # Resize frame to match VGG16 input size
    resized_frame = cv2.resize(frame, (224, 224))
    
    # Preprocess frame
    img_array = np.expand_dims(resized_frame, axis=0)
    img_array = preprocess_input(img_array)

    # Predict
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=1)[0]

    return {
        'prediction': decoded_predictions[0][1],
        'confidence': float(decoded_predictions[0][2]) * 100
    }

# Open camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to capture frame from camera")
        break

    # Classify frame
    result = classify_frame(frame)

    # Display result
    cv2.putText(frame, f"{result['prediction']} ({result['confidence']:.2f}%)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow('Classified Frame', frame)

    # Exit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()
