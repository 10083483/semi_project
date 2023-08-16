import streamlit as st
from utils import st_manual_desc as stmd


def app():
    st.header('Streamlit 매뉴얼')
    stmd.desc()


