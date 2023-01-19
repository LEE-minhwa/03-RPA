from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui
import pyperclip

keyword = pyautogui.prompt("키워드를 입력하세요>>>")
add_neighbor = 10 # 총 이웃 신청 개수
input_message = "관심있게 보고있습니다. 서로 이웃추가해요~"
count = 0 # 현재 이웃 신청 개수
index = 0 # 현재 블로그 글 번호

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5) # 웹페이지가 로딩 될 때까지 5초는 기다림
driver.maximize_window()

# 네이버 로그인
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
pyperclip.copy('dhi01')
pyautogui.hotkey('ctrl','v')
time.sleep(1)
pw= driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
pyperclip.copy('1994l03m09h')
pyautogui.hotkey('ctrl','v')
time.sleep(1)
# 로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR, "#log\.login")
login_btn.click()

# 웹페이지 해당 주소 이동
driver.get(f"https://m.search.naver.com/search.naver?where=m_blog&sm=mtb_opt&query={keyword}&sm=mtb_viw.blog&nso=so%3Add%2Cp%3Aall")
time.sleep(1)

while count < add_neighbor:
    # 이웃 아이디 선택
    ids = driver.find_elements(By.CSS_SELECTOR, ".sub_txt.sub_name")
    time.sleep(1)

    # 블로그 아이디 클릭
    # 현재 블로그 글 번호에 맞는 아이디 찾기
    id = ids[index]

    # 새창으로 열기
    id.send_keys(Keys.CONTROL + '\n')
    time.sleep(1)
    # 새창으로 드라이버 전환
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[1])

    try: # 예외 경우 제외
        # 이웃 추가 버튼 클릭
        driver.find_element(By.CSS_SELECTOR, "#root > div.blog_cover__Il6gZ > div > div.btn_area__OtwBw > div:nth-child(1) > button").click()
        time.sleep(1)
        # 서로 이웃 버튼 클릭
        driver.find_element(By.CSS_SELECTOR, "#bothBuddyRadio").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#buddyAddForm > fieldset > div > div.set_detail_t1 > div.set_detail_t1 > div > textarea").clear()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#buddyAddForm > fieldset > div > div.set_detail_t1 > div.set_detail_t1 > div > textarea").send_keys(input_message)
        time.sleep(1)

        # 확인 버튼 클릭
        driver.find_element(By.CSS_SELECTOR, ".btn_ok").click()
        time.sleep(2)
        
        count = count + 1
        print(f"{count}명 추가되었습니다.")
    except:
        pass
        driver.close()
    
    # 새창 닫기
    driver.close()
    # 기존 창으로 드라이버 전환
    driver.switch_to.window(all_windows[0])
    index = index + 1

    
# before_h = driver.execute_script("return window.scrollY")
# while True:
#     # 맨 아래로 스크롤을 내린다.
#     driver.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.END)

#     # 스크롤 사이 페이지 로딩 시간
#     time.sleep(1)

#     # 스크롤 후 높이
#     after_h = driver.execute_script("return window.scrollY")
#     if after_h == before_h:
#         break
#     before_h = after_h