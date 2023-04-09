from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import unicodedata
import pyautogui
import pyperclip

driver = webdriver.Chrome('chromedriver.exe')

tags = ['헬스', '운동스타그램', 'running', '오운완' , '일상' , '운동하는직장인', '기록']
#comments = ['♡', '원하는 댓글을', '리스트 형태로 입력', '우리 서로 맞팔해요~']

## 로그인 함수
def login(id, password):
    print('로그인 진행중...')
    driver.implicitly_wait(6)
    #ur_id = driver.find_element_by_xpath('//input[@aria-label="전화번호, 사용자 이름 또는 이메일"]')
    #ur_id.send_keys(id)
    ur_id = driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input")
    ur_id.click()
    pyperclip.copy(id)
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)
    #ur_password = driver.find_element_by_xpath('//input[@aria-label="비밀번호"]')
    #ur_password.send_keys(password)
    ur_password = driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > label > input")
    ur_password.click()
    pyperclip.copy(password)
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)
    ur_password.send_keys(Keys.ENTER)
    time.sleep(random.randrange(5,10))
    print("로그인 완료")

def detect_ad():
    ad_list = ['아이디 입력', '재테크', '투자', '부업', '집테크', '고수입', '수입', '억대연봉', '억대', '연봉', '순수익', '초기금액', '초기 금액', '금액', '입금']
    article = driver.find_elements_by_xpath('//article//div[1]/span')
    for texts in article :
        text = unicodedata.normalize('NFC',texts.get_attribute('innerText'))
        for ad in ad_list :
            if text.find(ad) == -1 :
                continue
            else :
                print(f'광고 발견. 발견된 광고단어 : {ad}')
                return True
            
def click_likebtn(like_num, stop_num):
    like_btn = driver.find_element_by_xpath('//*[@aria-label="좋아요" or @aria-label="좋아요 취소"] //ancestor :: button')
    like_svg = like_btn.find_element_by_tag_name('svg').get_attribute('aria-label')
    
    if like_svg == '좋아요' : 
        like_btn.click()
        like_num += 1 
        print(f'좋아요 {like_num}번째')
        #comment(comments[random.randrange(len(comments))])
        time.sleep(random.randrange(50, 61))
        return like_num, stop_num
    
    else :
        stop_num += 1
        print(f'이미 좋아요 작업한 피드 : {stop_num}개 중복')
        time.sleep(random.randrange(3, 10))
        return like_num, stop_num

def comment(text):
    tringer = random.randrange(1,5)
    if tringer != 3:
        return
    try : 
        comment_path = driver.find_element_by_xpath('//textarea[@aria-label="댓글 달기..."]')
        pass
    except :
        print('댓글이 제한된 피드입니다.')
        return
    comment_path.click()
    comment_path = driver.find_element_by_tag_name('textarea')
    driver.implicitly_wait(1)
    comment_path.send_keys(f'{text}')
    comment_path.send_keys(Keys.ENTER)
    print(f'댓글을 달았습니다. 내용 : {text}')
    time.sleep(3)

def next_btn():
    driver.find_element_by_xpath('//*[@aria-label="다음"] //ancestor :: button').click()

def bot(insta_tag, how_many): 
    driver.get('https://www.instagram.com/explore/tags/{}/'.format(insta_tag))
    driver.implicitly_wait(6)
    
    #new_feed = driver.find_element_by_xpath('//article//img //ancestor :: div[2]')
    
    new_feed = driver.find_element(By.CSS_SELECTOR, "#mount_0_0_pg > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div._a3gq._ab-1 > section > main > article > div._aaq8 > div > div > div:nth-child(1) > div:nth-child(2) > a > div")
    
    new_feed.click()
    driver.implicitly_wait(10)
    
    like = 0
    stop = 0
    
    for click in range(how_many):
        if detect_ad() == True:
            next_btn()
            driver.implicitly_wait(10)
        else :
            like, stop = click_likebtn(like, stop)
            next_btn()
            driver.implicitly_wait(10)
            
            if stop >= 4 :
                break


## main문
driver.get('https://instagram.com')
login('dhi01@naver.com','1994l03m09h!') ## !@로그인 정보 
random.shuffle(tags)

for tag in tags:
    try : 
        print(f'작업 태그는 \'{tag}\'입니다.')
        bot(tag, random.randrange(15,30))
        print(f'\'{tag}\' 태그 작업완료')
        time.sleep(random.randrange(600, 1800))
    except :
        print('새로운 피드가 없거나, 다음 피드가 없습니다. 다음 태그로 넘어갑니다.')
        time.sleep(random.randrange(5,10))
        driver.refresh()
driver.quit()