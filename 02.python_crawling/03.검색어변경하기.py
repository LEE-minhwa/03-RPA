import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요>>>")
response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}")
# print(response.status_code) ## 200은 통신상태 정상, 404는 페이지를 찾을 수 없음
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# soup.select_one("선택자")
# soup.select("선택자")

#results = soup.select("div.news_wrap.api_ani_send > div > a")
results = soup.select(".news_tit")
for result in results:
    title = result.text
    link = result.attrs['href']
    print(title, link)

    # pyinstaller -w -F 03.python.py