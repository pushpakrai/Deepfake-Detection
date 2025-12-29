import cv2
import numpy as np

def preprocess_image(image):
    image = cv2.resize(image, (224, 224))  # Resize to match model input size
    image = image / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image.astype(np.float32)
