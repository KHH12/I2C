import cv2
import pytesseract
import RPi.GPIO as GPIO
import time

motor_pin = 2

# GPIO 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_pin, GPIO.OUT)
pwm = GPIO.PWM(motor_pin, 50)
pwm.start(11.0)

# 이미지에서 숫자를 인식하는 함수
def recognize_numbers(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    numbers = pytesseract.image_to_string(gray, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    return numbers

# 숫자만 추출하는 함수
def extract_numbers(text):
    numbers_only = ''.join(c for c in text if c.isdigit())
    return numbers_only

# 서보 모터 동작 함수
def servo_action(scale):
    if scale == 1:
        angle = 90
    elif scale == 2:
        angle = 60
    elif scale == 3:
        angle = 30
    elif scale == 4:
        angle = 120
    elif scale == 5:
        angle = 90
    else:
        angle = 90
   
    duty_cycle = angle / 10
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1.0)

# 카메라 캡처 객체 생성
cap = cv2.VideoCapture(0)

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    # 프레임 읽기 실패 시 종료
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    # 숫자 인식
    numbers = recognize_numbers(frame)

    # 숫자만 추출
    numbers = extract_numbers(numbers)

    # 인식된 숫자가 있을 경우 서보 모터 동작
    if numbers:
        scale = int(numbers)
        servo_action(scale)

    # 화면에 인식된 숫자 출력
    cv2.putText(frame, numbers, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Number Recognition', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료 시 비디오 캡처 객체와 창 해제
cap.release()
cv2.destroyAllWindows()
GPIO.cleanup()