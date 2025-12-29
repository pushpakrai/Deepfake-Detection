import tensorflow as tf
import numpy as np
from utils.preprocessing import preprocess_image

# Load the H5 Model
MODEL_PATH = r"D:\deepfake_detection _1\model\deepfake_model.h5"  # Update path as needed
model = tf.keras.models.load_model(MODEL_PATH)

def predict_frame(frame, threshold=0.47, fake_range=(0.49, 0.51)):
    input_data = preprocess_image(frame)
    prediction = model.predict(input_data)[0][0]
    if fake_range[0] <= prediction <= fake_range[1]:
        return "Uncertain", prediction
    elif prediction >= threshold:
        return "Fake", prediction
    else:
        return "Real", prediction

def predict_multiple_frames(frames, threshold=0.47, fake_range=(0.49, 0.51)):
    confidences = [predict_frame(frame, threshold, fake_range)[1] for frame in frames]
    avg_confidence = np.mean(confidences)

    # Adjust threshold based on the average confidence
    if avg_confidence < 0.475:
        final_consistency = "Real"
    elif avg_confidence > 0.47:
        final_consistency = "Fake"
    else:
        final_consistency = "Uncertain"

    return final_consistency, avg_confidence, confidences
