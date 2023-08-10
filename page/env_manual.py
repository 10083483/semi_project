import streamlit as st
from utils import env_manual_desc as envmd


def app():
    st.header('가상환경 구축 매뉴얼')
    
    envmd.desc()

