import streamlit as st
import pandas as pd
from PIL import Image
import os
import pickle
import numpy as np
#from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

st.set_page_config(layout = "wide", page_icon = 'icon.jpg', page_title='Solar Panel Dust Detection')

st.header("Dust Detection in Solar Panels")
st.write('<p style="font-size:160%">Import the image:</p>', unsafe_allow_html=True)

image = st.file_uploader(label = '', type=["jpg", "jpeg", "png"])

if image:
    image = Image.open(image)
    st.image(image)
    image = image.resize((64, 64))
    grayscale_image = image.convert('L')
    pixel_value = list(grayscale_image.getdata())
    
    
    with open('rf_model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    pixel_value = np.array(pixel_value)
    
    prediction = model.predict(pixel_value.reshape(1, -1))
    ans = prediction[0]

    st.write('Result:',ans)
