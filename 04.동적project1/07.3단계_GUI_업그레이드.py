from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import requests
import json
import os

UI_PATH = "05.동적project1/design.ui"
sub_list = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(UI_PATH, self)
        self.pushButton_2.clicked.connect(self.search_start)
        self.pushButton_4.clicked.connect(self.search_reset)
        self.pushButton_3.clicked.connect(self.save)
        self.pushButton.clicked.connect(self.end)
    
    def search_start(self):
        self.label_3.setText("자동완성 키워드 추출을 시작합니다...")
        QApplication.processEvents()
        main_keyword = self.lineEdit.text()
        for sub in sub_list:
            keyword = main_keyword + ' '+ sub
            response = requests.get(f"https://ac.search.naver.com/nx/ac?q={keyword}&con=0&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100&_callback=_jsonp_5")

            origin_data = response.text
            dic_data = json.loads(origin_data.split("_jsonp_5(")[1][:-1])
            for data in dic_data['items'][0]:
                self.textBrowser.append(data[0])

        self.label_3.setText("자동완성 키워드 추출이 완료되었습니다.")
    
    def search_reset(self):
        self.textBrowser.setText("")
        self.lineEdit.setText("")
        self.label_3.setText("리셋 되었습니다.")
    
    def save(self):
        result = self.textBrowser.toPlainText()
        f = open(f'{self.lineEdit.text()}_연관검색어.text','w',encoding = 'utf-8')
        f.write(result)
        f.close
        self.label_3.setText(os.getcwd() + f'\{self.lineEdit.text()}_연관검색어.text 에 저장되었습니다.')
    
    def end(self):
        sys.exit()

QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

sys.exit(app.exec_())

#pyinstaller -w -F qtextbrowser_advanced.py