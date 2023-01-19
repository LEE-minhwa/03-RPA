import pyautogui
import time

# 1. 화면 크기 출력
# print(pyautogui.size())

# 2. 마우스 위치 출력
# time.sleep(2)
#print(pyautogui.position())

# 3. 마우스 이동
# 한번에 이동
#pyautogui.moveTo(300,200)

# a초 만큼 이동
#pyautogui.moveTo(300,200, 2)

# 4. 마우스 클릭
pyautogui.moveTo(-570,18, 2)
pyautogui.click()

# 5. 마우스 드래그
pyautogui.dragTo(100,200,2)