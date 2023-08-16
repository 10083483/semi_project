import streamlit as st
from utils import pjr_diagram_desc as dgrd


def app():
    st.header('프로젝트 diagram')
    dgrd.desc()

