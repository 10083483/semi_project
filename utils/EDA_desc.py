import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



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
    #g1-1
    fig, ax = plt.subplots()
    ax.bar(categories, values)
    plt.xlabel('Period')
    plt.ylabel('Sales Amount in trillion')
    plt.title('Sales Amount')
    plt.text(-0.33,values[0],str(values[0]), color='black', fontsize=14)
    plt.text(0.64, values[1],str(values[1]), color = 'black', fontsize = 14)#str(format(values[1], ","))
    st.pyplot(fig)
    st.write('''jdghjyjt''')
	
    #g1-2
    categories2 = ['During Covid19 Restriction', 'After Covid19 Restriction']
    values2 = [BeforeCOVID19_1.sum()['audiCnt']/1000000,AfterCOVID19_1.sum()['audiCnt']/1000000]
    st.write(values)
    fig2, ax2 = plt.subplots()
    ax2.bar(categories2 ,values2)
    plt.xlabel('Period')
    plt.ylabel('audience count in billion')
    plt.title('Audience Count')
    plt.text(-0.33,values2[0],str(values2[0]), color='black', fontsize=14)
    plt.text(0.64, values2[1],str(values2[1]), color = 'black', fontsize = 14)  
    st.pyplot(fig2)
    st.write('''jdghjyjt''')
	
    st.header('2. 코로나19로 인한 사회적 거리두기 기간과 그 이후의 오프라인 영화 프로모션 기사보도 추이 ')
    
    st.write('''
    먼저, 하기와 같이 코로나19로 인한 사회적 거리두기 기간을 구분하였습니다.
    
            코로나19 사회적 거리두기 발효일: 2021년 3월 1일
    코로나19 사회적 거리두기 종료일: 2022년 4월 18일

이후, 빅카인즈(Big Kinds) 웹페이지를 통해 하기와 같이 각 기간 별 기사 보도의 횟수를 전체 파악하였습니다.
총합은 
		'''
		)
    Newsresult = 'data/Newsresult.xlsx'
    
    required_cols = [1]
    GV = pd.read_excel(Newsresult, usecols = required_cols)
    threshold = 20220418        # 거리두기 완화 일자
    lower_count = GV[GV['일자'] < threshold].shape[0]
    higher_count = GV[GV['일자'] >= threshold].shape[0]
    
    print(lower_count)      # 거리두기 시기 '무대인사', '개봉' 키워드 관련 뉴스
    print(higher_count)     # 거리두기 완화 이후의 '무대인사', '개봉' 키워드 관련 뉴스
    
    categories_jw = ['During Covid19 Restriction', 'After Covid19 Restriction']
    values_jw = [lower_count, higher_count]
    fig_jw, ax = plt.subplots()
    ax.bar(categories_jw, values_jw)
    
    plt.bar(categories_jw, values_jw)
    
    plt.xlabel('Period')
    plt.ylabel('News')
    plt.title('News related to GV')
    
    plt.text(-0.05, 27, '42', color='k', fontsize = 14)
    plt.text(0.95, 237, '254', color = 'k', fontsize = 14)
    
    st.pyplot(fig_jw)
	
    st.header('3. ')
