import streamlit as st
from PIL import Image

def desc():
    img1 = Image.open('data/strm1.png')
    img4 = Image.open('data/strm4.png')
    img3 = Image.open('data/strm3.png')
    
    st.info('''streamlit 웹서버는 app.py 파일의 내용을 웹브라우저에 표출해준다.
            app.py 파일에 streamlit에서 제공하는 명령어들을 사용하여 원하는 내용을 웹브라우저에 표출시킬 수 있다.''', icon="ℹ️")
    st.subheader('1. 가상환경으로 진입')
    st.text('''
            명령어 'conda activate [ENV_NAME]'로 streamlit이 설치된 가상환경으로 진입한다. 
            app.py 파일이 있는 폴더로 이동한다. 
            ''')
    st.image(img1)
    st.text('app.py: 웹서버를 리스닝하며, 페이지 변경 요청이 왔을 때 페이지 구분을 해준다.'
            
            '\n   page 폴더의 파일들: app.py로부터 호출받아 클라이언트 역할을 하며, utils 폴더에 작성되는 모듈로부터 함수를 호출한다.'
            '\n   Utils 폴더의 파일들: page 폴더에 있는 파일들의 모듈로써, 파이선 코드로만 작성된 경우가 대부분이며 실제 코드를 작성해야 하는 부분이다.')
    
    st.subheader('2. 웹서버 실행')
    st.text('''
            명령어 'streamlit run [pyfile_NAME]'로 웹서버를 작동시킨다
            ''')
    st.image(img4)
    
    st.text('''
            이때 새창으로 웹페이지가 실행되며 콘솔에 나와있는 URL으로도 접속할 수 있다
            또한 파일 수정 후에도 app.py를 다시 실행시킬 필요없이 웹페이지만 새로고침하면 적용된다.
            ''')


    
    st.subheader('3. 웹서버 종료')
    st.text('''
            streamlit을 실행시킨 터미널(콘솔, powershell prompt)에서 ctrl + c 를 입력한다
            ''')
    st.image(img3)
    
  