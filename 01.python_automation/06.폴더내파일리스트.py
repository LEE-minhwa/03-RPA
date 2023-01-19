import os

# 2. 폴더 내 모든 파일 읽기

# dir_path = "C:/Users/이민화/Downloads"
# for (root, directories, files) in os.walk(dir_path):
#     for file in files:
#         #if '.txt' in file:
#             file_path = os.path.join(root, file)
#             print(file_path)

file_list = os.listdir("C:/Users/이민화/Downloads")

# 반복문 통해 각 파일의 확장자 확인
for file in file_list:
    name, ext = os.path.splitext(file)
    print(name)