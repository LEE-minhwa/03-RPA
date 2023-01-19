from cgitb import text
import os

# 정리할 확장자 리스트
image_list = ['.jpg', '.png', '.gif', '.jpeg', ".JPG"]
text_list = ['.hwp', '.docx', '.xlsx', '.xls', '.pdf']

# 정리할 폴더
target = "C:/Users/이민화/Downloads"

# 만들 폴더
image_fold = target + "/images"
text_fold = target + "/text"

# 폴더가 없다면 만들기
if not os.path.exists(image_fold):
    os.mkdir(image_fold)
if not os.path.exists(text_fold):
    os.mkdir(text_fold)

file_list = os.listdir(target)

# 반목문을 통해 각 파일의 확장자 확인
for file in file_list:
    name, ext = os.path.splitext(file)
    if ext in image_list:
        # 파일 이동
        source = os.path.join(target,file)
        print(source)
        os.rename(source, os.path.join(image_fold, file))
    elif ext in text_list:
        source = os.path.join(target,file)
        print(source)
        os.rename(source, os.path.join(text_fold, file))
