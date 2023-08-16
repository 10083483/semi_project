import streamlit as st
from PIL import Image

def desc():
    img1 = Image.open('data/env1.png')
    img21 = Image.open('data/env2-1.png')
    img22 = Image.open('data/env2-2.png')
    img31 = Image.open('data/env3-1.png')
    img32 = Image.open('data/env3-2.png')
    img4 = Image.open('data/env4.png')
    
    st.subheader('1. 현재 가상환경 리스트 확인')
    st.text('''
            anaconda powershell prompt 실행해 
            명령어 'conda env list'를 입력한다''')
    st.image(img1)

    st.subheader('2. 가상환경 생성')
    st.text('''
            명령어 'conda create --name [ENV_NAME]'를 입력한다
            ''')
    st.image(img21)
    st.text('''
            이떄 proceed?가 나오면 y를 입력한다
            ''')
    st.image(img22)
    
    st.subheader('3. 가상환경 실행,종료')
    st.text('''
            명령어 'conda activate [ENV_NAME]'으로 가상환경 실행
            'conda deactivate'으로 가상환경 종료
            ''')
    st.image(img31)
    st.info('파일 디렉토리 앞의 ()가 가상환경 이름으로 나오면 가상환경에 진입한 상태이다', icon="ℹ️")
    st.image(img32)
    
    st.subheader('4. 가상환경 삭제')
    st.text('''
            명령어 'conda remove --name [ENV_NAME] --all]'으로 가상환경 삭제
            ''')
    st.image(img4)