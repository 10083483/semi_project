import streamlit as st
from PIL import Image
def desc():

    img = Image.open('data/prj_diagram.png')
    st.image(img)