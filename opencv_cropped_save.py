#얼굴인식 크롭 이미지저장
import cv2

# haarcascade 불러오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

imgNum = 0
# 이미지 불러오기
img = cv2.imread('sisa1.jpg') # 이미지 파일 삽입 부분
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 얼굴 찾기
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cropped = img[y - int(h/4):y + h + int(h/1), x - int(w/4):x + w + int(w/4)] #상:하, 좌:우

    # 이미지를 저장
    cv2.imwrite("thumbnail" + str(imgNum) + ".png", cropped)
    imgNum += 1

cv2.waitKey(0)
cv2.destroyAllWindows()
