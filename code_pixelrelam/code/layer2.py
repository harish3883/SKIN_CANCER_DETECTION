from keras.models import load_model
from keras.preprocessing import image
import numpy as np

# Load the saved model
model = load_model("D:/Desktop/Charma/layer1/keras_model.h5")

# Load and preprocess the input image
img_path = "D:/Desktop/shirts/plain+shirts+for+men_8.jpg"
img = image.load_img(img_path, target_size=(224, 224))  # Adjust target_size according to your model's input size
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0  # Normalize the image data

# Make predictions
predictions = model.predict(img_array)

# Display the predictions
print(predictions)
