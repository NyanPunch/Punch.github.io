import cv2
import os

# 2. os.listdir 이용
file_list = os.listdir('.\\images') # 특정 폴더에 있는 이미지 파일 목록을 불러온다.
img_files = [file for file in file_list if file.endswith('.jpg')] #jpg로 되어있는 파일을 불러옴

for f in img_files:
    print(f)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_AUTOSIZE , cv2.WINDOW_AUTOSIZE)

# 슬라이드 쇼 반복을 위한 반복문
count = len(img_files)
index = 0

while True:
    img = cv2.imread(img_files[index])

    # 예외처리
    if img is None:
        print("이미지를 불러오는데 실패했습니다.")
        break

    # ESC가 입력되면 break
    cv2.imshow('image', img)
    if cv2.waitKey(1000) == 27:
        break

    # index가 이미지 리스트보다 커지거나 같아지면 다시 0으로
    index += 1
    if index >= count:
        index = 0

cv2.destroyAllWindows()
