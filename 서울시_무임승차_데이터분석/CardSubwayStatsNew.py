import requests  
from bs4 import BeautifulSoup as bs  
import pandas as pd

def request_url(urldate, endpage=5):   # url 생성 함수
    user_key="4d6d534d717764633738714b704f59"
    url="http://openapi.seoul.go.kr:8088/" + user_key
    url=url + "/xml/CardSubwayStatsNew/1/"+ str(endpage) # 출력 데이터 개수
    url=url + "/" + str(urldate)    # 조회 날짜

    subway_html=requests.get(url)  # 생성된 url을 기준으로 요청

    if subway_html.status_code != 200: # 데이터를 받아오지 못했다면 종료
        exit("데이터를 받지 못함")
    
    return subway_html


def swdataframe(schdate):   # 요청데이터를 이용해 DataFrame으로 제공 함수
    subway_html=request_url(schdate)
    #print(subway_html.text)
    soup=bs(subway_html.text, "html.parser")

    endpage=soup.find('list_total_count').get_text()

    subway_html=request_url(schdate, endpage)
    soup=bs(subway_html.text, "html.parser")

    rows=soup.find_all("row")

    sw=[]
    for row in rows:
        use_dt=row.find('use_dt').get_text()
        line_num=row.find('line_num').get_text()
        sub_sta_nm=row.find('sub_sta_nm').get_text()
        ride_pasgr=row.find('ride_pasgr_num').get_text()
        alight_pasgr=row.find('alight_pasgr_num').get_text()

        sw.append([use_dt, line_num, sub_sta_nm, ride_pasgr, alight_pasgr])

    swdf=pd.DataFrame(sw, columns=["사용일자", "호선명", "역명", "승차인원", "하차인원"])
    
    return swdf

# 현재 위치에서 실행시에만 아래 코드가 실행
# 즉 다른 파일에서 호출하면 실행 안됨

if __name__ == "__main__":  
    schdate=input("조회일을 입력하세요.(예:20220101):")
    df1=swdataframe(schdate)
    df1.head()