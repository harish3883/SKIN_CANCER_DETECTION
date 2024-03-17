import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Replace with the correct path to the directory containing saved_model.pb
saved_model_path = "D:/Downloads/converted_savedmodel/model.savedmodel"
loaded_model = tf.saved_model.load(saved_model_path)

# Load and preprocess the new input image
img_path = "D:/Desktop/shirts/plain+shirts+for+men_1.jpg"
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = tf.keras.applications.mobilenet.preprocess_input(img_array)


predictions = loaded_model(tf.constant(img_array, dtype=tf.float32))
predictions = list(predictions)
x=predictions.index(max(predictions))
if x=="0":
    print("Skin")
else:
    print("Other")

