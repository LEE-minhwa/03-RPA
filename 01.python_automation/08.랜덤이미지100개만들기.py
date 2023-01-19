import numpy
from PIL import Image
import os

# 만들 폴더 경로
target = "C:/Users/이민화/Desktop/Minhwa/자동화pjt/02.python_automation/random"

# 폴더 만들기
if not os.path.exists(target):
    os.mkdir(target)

for i in range(1, 101):
    filename = f'{i}.jpg'

    # 3차원 rgb 랜덤 배열 생성
    rgb_array = numpy.random.rand(720, 1080, 3) * 255

    # 이미지 생성
    image = Image.fromarray(rgb_array.astype('uint8')).convert('RGB')

    # 이미지 저장
    image.save(os.path.join(target, filename))