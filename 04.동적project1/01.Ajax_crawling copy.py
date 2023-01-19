import requests
import json
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요>>>")

dic = ['ㄱ','ㄴ','ㄷ','ㄹ']
response = requests.get(f"https://ac.search.naver.com/nx/ac?q={keyword}&_callback=_jsonp_20")

origin_data = response.text
dic_data = json.loads(origin_data.split("_jsonp_6(")[1][:-1])

for i in range(0,10,1):
    print(dic_data["items"][0][i][0])
