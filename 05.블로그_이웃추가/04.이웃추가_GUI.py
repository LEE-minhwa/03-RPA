from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import requests
import json
import os
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

UI_PATH = "C://Users//이민화//Desktop//Minhwa//자동화pjt//06.블로그_이웃추가//design.ui"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
Ui_MainWindow, QtbaseClass = uic.loadUiType(BASE_DIR + r'\design.ui')

class Mywindow(QMainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.ui = Ui_MainWindow()

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(UI_PATH, self)
        self.start_btn.clicked.connect(self.main)
        self.reset_btn.clicked.connect(self.reset)
        self.close_btn.clicked.connect(self.end)

    def main(self):
        input_id = self.id.text()
        input_pw = self.pw.text()
        input_keyword = self.keyword.text()
        input_max = self.max.value()
        input_message = self.message.toPlainText()

        # validation check(유효성 검사)
        if input_id == "" or input_pw == "" or input_keyword == "" or input_message =="":
            self.status.setText("빈칸을 채워주세요")
            return 0 # 함수 종료

        self.status.setText("로그인 진행중...")
        QApplication.processEvents()
        driver = self.login(input_id, input_pw)

        if driver == 0:
            self.status.setText("로그인 실패, 아이디 비밀번호 확인")
            return 0 # 함수 종료
        else:
            self.status.setText("로그인 성공!!")
            QApplication.processEvents()
            time.sleep(1)
            self.status.setText("이웃추가 진행중...")
            QApplication.processEvents()
            self.start(driver, input_keyword, input_max, input_message)
            self.status.setText("이웃추가 완료!!")
        

    def login(self, input_id, input_pw):
        # 브라우저 꺼짐 방지
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        # 불필요한 에러 메세지 없애기
        chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])

        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.implicitly_wait(3) # 웹페이지가 로딩 될 때까지 3초는 기다림
        driver.maximize_window()

        # 네이버 로그인
        driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
        id = driver.find_element(By.CSS_SELECTOR, "#id")
        id.click()
        
        pyperclip.copy(input_id)
        pyautogui.hotkey('ctrl','v')
        time.sleep(1)
        pw= driver.find_element(By.CSS_SELECTOR, "#pw")
        pw.click()
        
        pyperclip.copy(input_pw)
        pyautogui.hotkey('ctrl','v')
        time.sleep(1)
        login_btn = driver.find_element(By.CSS_SELECTOR, "#log\.login")
        login_btn.click()

        # 로그인 완료
        # 로그인 성공시 드라이버 반환
        # 로그인 실패시 함수 0 반환

        check = driver.find_elements(By.CSS_SELECTOR, "#minime" )
        if len(check) > 0:
            return driver
        else:
            driver.close()
            return 0

    def start(self, driver, input_keyword, input_max, input_message):
        # 키워드 시작
        driver.get(f"https://m.search.naver.com/search.naver?where=m_blog&sm=mtb_opt&query={input_keyword}&sm=mtb_viw.blog&nso=so%3Add%2Cp%3Aall")
        time.sleep(1)

        count = 0 # 현재 이웃 신청 개수
        index = 0 # 현재 블로그 글 번호

        while count < input_max:
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
            except:
                pass
                driver.close()
                driver.switch_to.window(all_windows[0])
                index = index + 1 # 현재 블로그 글 번호 증가
            
            # 새창 닫기
            driver.close()

            # 기존 창으로 드라이버 전환
            driver.switch_to.window(all_windows[0])
            index = index + 1 # 현재 블로그 글 번호 증가

        
    def reset(self):
        self.id.setText("")
        self.pw.setText("")
        self.keyword.setText("")
        self.message.setText("")
        self.status.setText("리셋 되었습니다.")
    
    def end(self):
        sys.exit()

QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

sys.exit(app.exec_())

#pyinstaller -w -F Naver_keyword.py