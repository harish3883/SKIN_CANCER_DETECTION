import streamlit as st
from PIL import Image
from ultralytics import YOLO
import numpy as np


st.title("Charma")
model = YOLO('D:/Desktop/Charma/code/best.pt')
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    results = model(image)  
    names_dict = results[0].names
    probs = results[0].probs.data.tolist()
    st.header(names_dict[np.argmax(probs)]+"  "+str(max(probs)*100)+'%')



        