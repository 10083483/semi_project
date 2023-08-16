import streamlit as st
from page import env_manual as envm
from page import st_manual as stm
from page import pjr_diagram as dgr
from page import EDA 
from page import intro

#st.title('Project')

item_list = ['item0','item1', 'item2', 'item3', 'item4']

item_labels = {'item0':'소개', 'item1':'가상환경 구축 매뉴얼', 'item2':'streamlit 매뉴얼', 
               'item3':'프로젝트 diagram', 'item4':'처리 및 분석'}

FIL = lambda x : item_labels[x]
item = st.sidebar.selectbox('항목을 골라요.',  item_list, format_func = FIL )

if item == 'item1':
	envm.app()
elif item == 'item2':
	stm.app()
elif item == 'item3':
	dgr.app()
elif item == 'item4':
	EDA.app()
elif item == 'item0':
	intro.app()
