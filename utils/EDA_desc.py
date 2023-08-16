import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def desc():

    st.title('처리 및 분석')
    st.header('1. boxoffice')
    
    BeforeCOVID19_1 =pd.read_csv('data/1.boxofficeD.csv',encoding='utf-8-sig')
    AfterCOVID19_1 =pd.read_csv('data/1.boxofficeA.csv',encoding='utf-8-sig')
    #st.dataframe(BeforeCOVID19_1)
    BeforeCOVID19_1 = BeforeCOVID19_1.astype({'salesAmt':'float','audiCnt':'float'})
    AfterCOVID19_1 = AfterCOVID19_1.astype({'salesAmt':'float','audiCnt':'float'})
    categories = ['During Covid19 Restriction', 'After Covid19 Restriction']
    values = [BeforeCOVID19_1.sum()['salesAmt'],AfterCOVID19_1.sum()['salesAmt']]
    
    fig, ax = plt.subplots()
    ax.bar(categories, values)
    
    plt.xlabel('Period')
    plt.ylabel('Sales Amount in trillion')
    plt.title('Sales Amount')
    
    plt.text(-0.33,values[0],str(values[0]), color='black', fontsize=14)
    plt.text(0.64, values[1],str(values[1]), color = 'black', fontsize = 14)#str(format(values[1], ","))
	
    st.pyplot(fig)
    
    st.write('''jdghjyjt''')
    
    st.header('2. ')
    st.header('3. ')
