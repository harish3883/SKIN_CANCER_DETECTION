import streamlit as st
from PIL import Image
from ultralytics import YOLO
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

def yolo():
    results = model(image)  
    names_dict = results[0].names
    probs = results[0].probs.data.tolist()
    st.header(str(names_dict[np.argmax(probs)])+"   "+str(max(probs)*100)+'%')

st.title("Charma")
model = YOLO('D:/Desktop/Charma/code/best.pt')
loaded_model = tf.saved_model.load( "D:/Downloads/converted_savedmodel/model.savedmodel")
uploaded_file = st.file_uploader("Choose an image...", type="jpg")
"""saved_model_path = "D:/Downloads/converted_savedmodel/model.savedmodel"
loaded_model = tf.saved_model.load(saved_model_path)"""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    """img = image.load_img(uploaded_file, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.mobilenet.preprocess_input(img_array)
    predictions = loaded_model(tf.constant(img_array, dtype=tf.float32))
    predictions = list(predictions)
    x=predictions.index(max(predictions))"""
    x=0
    if x==0:
        yolo()
    else:
        st.header("Please give an image that has skin or damaged skin")



        