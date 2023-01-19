import requests
import json
import pyautogui

main_keyword = pyautogui.prompt("키워드를 입력하세요>>>")
sub_list = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

f = open(f'05.동적project1/{main_keyword}.txt','w', encoding='utf-8')

for sub in sub_list:
    keyword = main_keyword + ' '+ sub
    response = requests.get(f"https://ac.search.naver.com/nx/ac?q={keyword}&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100&_callback=_jsonp_5")

    origin_data = response.text
    dic_data = json.loads(origin_data.split("_jsonp_5(")[1][:-1])
    f.write(f"=========={sub}으로 시작하는 검색어==========" + '\n')
    for data in dic_data['items'][0]:
        print(data[0])
        f.write(data[0] + '\n')

f.close()
