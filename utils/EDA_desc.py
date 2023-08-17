import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def desc():

    st.title('처리 및 분석')
    st.header('1. 코로나19로 인한 사회적 거리두기 기간과 그 이후의 영화관 매출액과 관객수 변화')
    st.write('''
    먼저, 하기와 같이 코로나19로 인한 사회적 거리두기 기간을 구분하였습니다. 
    
            During Covid19 Restriction: 사회적 거리두기 발효일(21.3.1)부터 종료 전일(22.4.17)까지 약 412일
    After Covid19 Restriction: 사회적 거리두기 종료일(22.4.18)부터 23.5.4까지 약 412일

이후, 영화진흥위원회(KOFIC)의 오픈 API를 활용하여 코로나19 사회적 거리두기 기간과, 거리두기가 완화된 이후의 현재까지의 일간 박스오피스를 취합해 기간중 영화별 누적 관객 수, 누적 매출액 등을 수집하였습니다

		'''
		)
    st.write('''
             ```
def boxoffice(date_start,date_end1):

    yourkey='f5eef3421c602c6cb7ea224104795888'
    date_end = datetime.datetime.strptime(date_end1, '%y%m%d')
    date_str = date_string(date_end)

    movie_list = []
    date_list =[]
    
    while date_str != date_start:
        date_end = date_end - timedelta(days=1)
        date_str = date_string(date_end)
        #print(date_str)
        url = 'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key='+yourkey+'&targetDt='+date_str
        resp = requests.get(url)
        sh_date=resp.json()['boxOfficeResult']['showRange'][:8] #박스오피스 일자 추출
        date_list.append(sh_date)
        data = resp.json()['boxOfficeResult']['dailyBoxOfficeList']# 일간 박스오피스 추출
        movie_list.extend(data) #movie_list에추가

    df = pd.DataFrame(movie_list)
    df = df.astype({'salesAmt':'float','audiCnt':'float'})
    pd.options.display.float_format = '{:.1f}'.format
    mydict = {"salesAmt":"sum", "audiCnt":"sum"}    #컬럼이름(키 값)이 같으면 안됨
    results=df.groupby("movieNm").agg(mydict)   # 영화이름(movieNm)기준으로 묶어서 mydict 안의 계산을 칼럼별로 실행
    results.insert(0,"startDate",date_start)    #0열에 startDate라는 열을 집어넣고 값을 date_start로 저장
    results.insert(1,"endDate",date_list[0])
    df.to_csv(csvFileName, mode='a', encoding='utf-8', index=False) #추출 결과를 csv파일로 저장
    return results
    ```
    ''')
    st.write('''
    여기서 얻은 거리두기 시기, 그리고 완화 이후 시기의 영화별 누적 매출액,누적 관객 수를 그래프화하기 위해 아래와 같이 코딩하였습니다.
    ```
    categories = ['During Covid19 Restriction', 'After Covid19 Restriction']
    values = [ round(BeforeCOVID19_1.sum()['salesAmt']/1000000000, 1),round(AfterCOVID19_1.sum()['salesAmt']/1000000000, 1)]
    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax1.bar(categories, values)
    plt.xlabel('Period')
    plt.ylabel('Sales Amount in billion')
    plt.title('Sales Amount')
    plt.text(-0.33,values[0],str(values[0]), color='black', fontsize=14)
    plt.text(0.64, values[1],str(values[1]), color = 'black', fontsize = 14)
    plt.xticks(rotation=10)
    
    st.pyplot(fig)
    ```
		'''
		)

    BeforeCOVID19_1 =pd.read_csv('data/1.boxofficeD.csv',encoding='utf-8-sig')
    AfterCOVID19_1 =pd.read_csv('data/1.boxofficeA.csv',encoding='utf-8-sig')
    #st.dataframe(BeforeCOVID19_1)
    BeforeCOVID19_1 = BeforeCOVID19_1.astype({'salesAmt':'float','audiCnt':'float'})
    AfterCOVID19_1 = AfterCOVID19_1.astype({'salesAmt':'float','audiCnt':'float'})
    
    #####
    categories = ['During Covid19 Restriction', 'After Covid19 Restriction']
    values = [ round(BeforeCOVID19_1.sum()['salesAmt']/1000000000, 1),round(AfterCOVID19_1.sum()['salesAmt']/1000000000, 1)]
    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax1.bar(categories, values)
    plt.xlabel('Period')
    plt.ylabel('Sales Amount in billion')
    plt.title('Sales Amount')
    plt.text(-0.33,values[0],str(values[0]), color='black', fontsize=14)
    plt.text(0.64, values[1],str(values[1]), color = 'black', fontsize = 14)
    plt.xticks(rotation=10)
    
    ax2 = fig.add_subplot(122)
    categories2 = ['During Covid19 Restriction', 'After Covid19 Restriction']
    values2 = [ round(BeforeCOVID19_1.sum()['audiCnt']/1000000, 1),round(AfterCOVID19_1.sum()['audiCnt']/1000000, 1)]
    ax2.bar(categories2 ,values2)
    plt.xlabel('Period')
    plt.ylabel('audience count in million')
    plt.title('Audience Count')
    plt.text(-0.33,values2[0],str(values2[0]), color='black', fontsize=14)
    plt.text(0.64, values2[1],str(values2[1]), color = 'black', fontsize = 14)  
    plt.xticks(rotation=10)
    st.pyplot(fig)

    
    ####

	
    st.header('2. 코로나19로 인한 사회적 거리두기 기간과 그 이후의 오프라인 영화 프로모션 기사보도 추이 ')
    
    st.write('''
    먼저, 하기와 같이 코로나19로 인한 사회적 거리두기 기간을 구분하였습니다.
    
            코로나19 사회적 거리두기 발효일: 2021년 3월 1일
    코로나19 사회적 거리두기 종료일: 2022년 4월 18일

이후, 빅카인즈(Big Kinds) 웹페이지를 통해 하기와 같이 각 기간 별 개봉 영화의 오프라인 프로모션 기사 보도의 횟수를 전체 파악하였습니다. 이 때 사용한 키워드는 '무대인사', 그리고 연극 및 포토 뉴스의 중복을 피하기 위해 추가적으로 "개봉" 키워드를 반드시 포함하도록 사용하였습니다.
전체 자료 중 제가 구하고자 하는 것은 사회적 거리두기 기간과, 거리두기가 완화된 이후의 오프라인 프로모션 빈도수이므로 '일자'를 기준으로 기간을 2분할 하였습니다. 
		'''
		)
    st.write('''
             ```
    Newsresult = 'data/Newsresult.xlsx'
    
    required_cols = [1]
    GV = pd.read_excel(Newsresult, usecols = required_cols)
    threshold = 20220418        # 거리두기 완화 일자
    lower_count = GV[GV['일자'] < threshold].shape[0]
    higher_count = GV[GV['일자'] >= threshold].shape[0]
    print(lower_count)      # 거리두기 시기 '무대인사', '개봉' 키워드 관련 뉴스
    print(higher_count)     # 거리두기 완화 이후의 '무대인사', '개봉' 키워드 관련 뉴스
    ```
    ''')
    st.write('''
    여기서 얻은 거리두기 시기, 그리고 완화 이후 시기의 기사 보도 개수를 그래프화하기 위해 아래와 같이 코딩하였습니다.
    ```
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
    ```
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
	
    st.header('3. 코로나19로 인한 사회적 거리두기 기간과 그 이후의 OTT 서비스 사용량 변화 추이')
    st.write('''
    코로나19로 인한 사회적 거리두기 기간을 구분.
    ```
    코로나19 사회적 거리두기 발효일: 2021년 3월 1일
    코로나19 사회적 거리두기 종료일: 2022년 4월 18일
    ```
    사회적 거리두기 발효일 과 종료일 사이 기간동안의 OTT 서비스 가입자 및 사용자 변화 추이를 알아봤습니다.
    수집한 자료에서 날짜, OTT 서비스 맴버십 가입자, 수입(매출) 을 기준으로 구분했습니다.
         '''
    )
    st.write('''
    ```
    csv_file_path = 'data/netflix_revenue.csv' # CSV 파일 경로 설정
    df = pd.read_csv(csv_file_path) # CSV 파일 읽기
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y') 
     # 날짜(Date)를 "DD-MM-YYYY" 형식으로 파싱
    ```
    ''')
    st.write('''
    ```그래프 그리기
    fig_sk, ax1 = plt.subplots(figsize=(10, 6))```
    
    Global Revenue 그래프 그리기 (ax1에 연결)
    ```ax1.plot(df['Date'], df['Global Revenue'], color='red', marker='o', label='Global Revenue')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Global Revenue', color='red')
    ax1.tick_params(axis='y', labelcolor='red')```

    Netflix Streaming Memberships 그래프 그리기 (ax2에 연결)
    ```ax2 = ax1.twinx()
    ax2.plot(df['Date'], df['Netflix Streaming Memberships '], color='blue', marker='o', label='Netflix Streaming Memberships')
    ax2.set_ylabel('Netflix Streaming Memberships', color='blue')
    ax2.tick_params(axis='y', labelcolor='blue')```

    그래프 타이틀 설정
    ```plt.title('Netflix Revenue and Memberships Over Time')```

    범례 표시
    ```lines = ax1.get_lines() + ax2.get_lines()
    labels = [line.get_label() for line in lines]
    plt.legend(lines, labels, loc='upper left')```

    그래프 표시
    ```plt.tight_layout()
    plt.grid(True)
    plt.show()
    st.pyplot(fig_sk)```
    ''')

      # CSV 파일 경로 설정
    csv_file_path = 'data/netflix_revenue.csv'

    # CSV 파일 읽기
    df = pd.read_csv(csv_file_path)

    # 날짜(Date)를 "DD-MM-YYYY" 형식으로 파싱
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

    # 그래프 그리기
    fig_sk, ax1 = plt.subplots(figsize=(10, 6))

    # Global Revenue 그래프 그리기 (ax1에 연결)
    ax1.plot(df['Date'], df['Global Revenue'], color='red', marker='o', label='Global Revenue')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Global Revenue', color='red')
    ax1.tick_params(axis='y', labelcolor='red')

    # Netflix Streaming Memberships 그래프 그리기 (ax2에 연결)
    ax2 = ax1.twinx()
    ax2.plot(df['Date'], df['Netflix Streaming Memberships '], color='blue', marker='o', label='Netflix Streaming Memberships')
    ax2.set_ylabel('Netflix Streaming Memberships', color='blue')
    ax2.tick_params(axis='y', labelcolor='blue')

    # 그래프 타이틀 설정
    plt.title('Netflix Revenue and Memberships Over Time')

    # 범례 표시
    lines = ax1.get_lines() + ax2.get_lines()
    labels = [line.get_label() for line in lines]
    plt.legend(lines, labels, loc='upper left')

    # 그래프 표시
    plt.tight_layout()
    plt.grid(True)
    plt.show()
    st.pyplot(fig_sk)
        
    st.header('4. 참고 자료')
    st.write('''
             ```
             < 코로나19 관련 정책 조사 >
전체 < 보도자료 < 뉴스 & 이슈 < 코로나바이러스감염증-19 (kdca.go.kr)

< 기사 수집 및 분석에 사용한 사이트 >
빅카인즈(BIG KINDS)

– 영상 관련 링크 - 

한국영상자료원 (KOFA): 한국 영화 산업에 관한 다양한 통계와 정보를 제공하는 기관입니다. 
영화 매출, 관객 수, 개봉 영화 수 등에 대한 데이터를 확인할 수 있습니다.
웹사이트: http://www.kofa.or.kr/

한국문화정보원 (KOFICE): 한국 문화 및 예술 산업의 통계와 보고서를 제공합니다. 
OTT 플랫폼의 성장과 영화 관련 데이터를 포함하고 있을 수 있습니다.
웹사이트: http://www.kofice.or.kr/

한국콘텐츠진흥원 (KOCOWA): 한국의 콘텐츠 산업 동향을 파악할 수 있는 정보를 제공하며, 
OTT 플랫폼과 관련된 데이터를 찾을 수 있을 것입니다.
웹사이트: https://www.kocowa.kr/

영화진흥위원회 (KOFIC): 대한민국 영화 산업의 통계와 정보를 제공하며, 
영화 관련 데이터를 확인할 수 있는 공식 기관입니다.
웹사이트: https://www.kofic.or.kr/



< 기간, 국가, 종류별 박스오피스 통계 >
KOFIC 영화관 입장권 통합전산망 :: 연도별 박스오피스 (kobis.or.kr)

<ott 관련 데이터>
https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=ott&operator=AND&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=_score&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage=1&perPage=10&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode=

유료로 이용 중인 온라인동영상서비스(OTT) (중복응답) (mediastat.or.kr) (20-22)

<영화상영관 현황>
https://www.data.go.kr/data/15045008/fileData.do
<서울특별시_대중문화활동 참여율 통계>
https://www.data.go.kr/data/15085136/fileData.do

<주간 / 주말 박스오피스 통계 API >
영화진흥위원회 오픈API (kobis.or.kr)

< 더 중앙 한국영화 침체 관련 뉴스 링크 >
왜 유독 더딜까, 영화계 코로나 회복률 10개국 중 9위 | 중앙일보 (joongang.co.kr)

```
'''
             )

