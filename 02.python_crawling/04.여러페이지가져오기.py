import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요>>>")
lastpage = int(pyautogui.prompt("마지막 페이지번호를 입력해 주세요 >>>"))
pageNum = 1
for page in range(1,lastpage*10,10):
    print(f"{pageNum}페이지 입니다=================")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={page}")
    # print(response.status_code) ## 200은 통신상태 정상, 404는 페이지를 찾을 수 없음
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.select(".news_tit")
    for result in results:
        title = result.text
        link = result.attrs['href']
        print(title, link)
    pageNum = pageNum + 1 