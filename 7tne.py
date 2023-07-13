import cv2
import numpy as np
from skimage.transform import resize
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras

# 학습된 모델을 LOAD
model = keras.models.load_model('My_MNIST_CNN_DATA.h5')
model.summary()

drawing = False  # True is Mouse Click
ix, iy = -1, -1

# Mouse Callback
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    if event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img, (x, y), 5, (255, 255, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, (x, y), 5, (255, 255, 255), -1)

def answer(img):
    img = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)
    test_num = img[:, :, 0]
    test_num = (test_num > 0.1) * test_num
    test_num = test_num.astype('float32')
    plt.imshow(test_num, cmap='Greys', interpolation='nearest')
    test_num = test_num.reshape((1, 28, 28, 1))
    prediction = model.predict(test_num)
    predicted_class = np.argmax(prediction)
    confidence = prediction[0][predicted_class] * 100
    print('Predicted Digit:', predicted_class)
    print('Confidence:', confidence, '%')

# 웹캠 스트림 열기
cap = cv2.VideoCapture(2)

# 창 생성 및 마우스 콜백 등록
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame from webcam")
        break

    # 화면에 표시할 이미지 복사
    img = frame.copy()

    # 이미지 출력
    cv2.imshow('image', img)

    # 키 입력 대기
    k = cv2.waitKey(1) & 0xFF

    # Backspace 키를 누르거나 그리지 않은 상태에서 숫자를 자동 인식
    if k == 8 or not drawing:
        answer(img)
        img = np.zeros(frame.shape, np.uint8)

    # ESC 키를 누르면 종료
    if k == 27:
        break

# 리소스 해제
cap.release()
cv2.destroyAllWindows()
