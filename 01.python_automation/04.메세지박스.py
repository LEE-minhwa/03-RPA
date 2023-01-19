import pyautogui

# 1. 알림
#pyautogui.alert("시작하시겠습니까?")

# 2. 입력창
page = pyautogui.prompt("몇 페이지까지 검색?")
print(page)