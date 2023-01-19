from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
import time

keyword = pyautogui.prompt("검색어를 입력하세요>>>")
# lastpage = int(pyautogui.prompt("마지막 페이지번호를 입력해 주세요 >>>"))
# pageNum = 1

browser = webdriver.Chrome('C:/chromedriver.exe')
browser.get('https://www.naver.com')
browser.implicitly_wait(10)
browser.find_element(By.CSS_SELECTOR,'a.nav.shop').click()
time.sleep(2)

# 검색창 클릭
search = browser.find_element(By.CSS_SELECTOR,'#_verticalGnbModule > div > div._header_header_REoTl > div > div._gnb_header_shop_Xd6Hq > div > div._gnbSearch_search_area_3LAyd > form > fieldset > div > input')
search.click()

# 검색어 입력
search.send_keys(keyword)
search.send_keys(Keys.ENTER)

before_h = browser.execute_script("return window.scrollY")
while True:
    # 맨 아래로 스크롤을 내린다.
    browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")
    if after_h == before_h:
        break
    before_h = after_h

# 상품 정보 div
items = browser.find_element(By.CSS_SELECTOR,"#__next > div > div.style_container__1YjHN > div.style_inner__18zZX > div.style_content_wrap__1PzEo > div.style_content__2T20F > ul > div > div:nth-child(25) > li > div > div.basicList_info_area__17Xyo")
print(items)
for item in items:
    name = item.browser.find_element(By.CSS_SELECTOR,".basicList_link__1MaTN").text
    try:
        price = item.browser.find_element(By.CSS_SELECTOR,".price_num__2WUXn").text
    except:
        price = "판매중단"
    link = item.browser.find_element(By.CSS_SELECTOR,".basicList_link__1MaTN > a").get_attribute("href")
    print(name, price, link)







