import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import tensorflow as tf

# Load the Keras model
model = tf.keras.models.load_model("model/deepfake_model.h5")

# Convert the model to TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TFLite model
with open("model/deepfake_model.tflite", "wb") as f:
    f.write(tflite_model)

print("Model successfully converted to TFLite!")
