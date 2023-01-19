import os
import shutil
import pathlib

# 1. 폴더 만들기
current_path = os.getcwd()
print("현재 위치 : " + current_path)
#os.mkdir("kimbob") 현재 위치에 만들기
#os.mkdir("/Users/dev/BlockDMask/Example/GoodFolder1") 절대 위치 폴더 만들기
#os.makedirs("a/b/c/d") 경로 상에 폴더다 만들기
#if not os.path.exists(C:/Users/이민화/Downloads/이미지 파일)
    # os.makedirs("C:/Users/이민화/Downloads/이미지 파일")

# os.makedirs("C:/Users/이민화/Downloads/이미지 파일")
# os.makedirs("C:/Users/이민화/Downloads/문서 파일")
# os.makedirs("C:/Users/이민화/Downloads/동영상 파일")


# 3. 확장자 추출하기
# path = pathlib.Path('/Users/user/Documents/sampledoc.docx')

# print('Parent:', path.parent)
# print('Filename:', path.name)
# print('Extension:', path.suffix)

# 4. 파일 이동하기
# source = "C:/Users/이민화/Downloads"
# files = os.listdir(source)
# print(files)

# 5. 폴더 정리하기
if not os.path.exists(C:/Users/이민화/Downloads/이미지 파일)
    os.makedirs("C:/Users/이민화/Downloads/이미지 파일")

source = "C:/Users/이민화/Downloads"

text_file = [".hwp", ".txt", ".xlsx", ".xls", ".docx"]
image_file = [".png", ".jpg", "jpeg"]

for (root, directories, files) in os.walk(source):
    for file in files:
        file_path = os.path.join(root, file)
        file_path = pathlib.Path(file)
        file_Extension = file_path.suffix
        print(file_Extension)
        for file_Extesnsion in text_file:
            if file_Extension == text_file:
                print("문서 파일입니다.")
                shutil.move(f"{source}/{file}","C:/Users/이민화/Downloads/문서 파일")
            else:
                print("기타 파일입니다.")
                shutil.move(f"{source}/{file}","C:/Users/이민화/Downloads/기타 파일")

        
