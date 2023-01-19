import requests
from bs4 import BeautifulSoup
import pyautogui

codes = [
]

for code in codes:
    response = requests.get(f"https://finance.naver.com/item/sise.naver?code={code}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal").text
    price = price.replace(',','')
    print(price)