import requests
from bs4 import BeautifulSoup

response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
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