import cv2
import pytesseract
from picamera.array import PiRGBArray
from picamera import PiCamera

# 이미지에서 숫자를 인식하는 함수
def recognize_numbers(image):
    # 이미지를 그레이스케일로 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 이미지에서 숫자를 인식
    numbers = pytesseract.image_to_string(gray, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

    return numbers

# Pi Camera 초기화
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
raw_capture = PiRGBArray(camera, size=(640, 480))

# 초기화 시간을 주기 위해 잠시 대기
time.sleep(0.1)

for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
    # 프레임 가져오기
    image = frame.array

    # 숫자 인식
    numbers = recognize_numbers(image)

    # 숫자만 추출하여 출력
    recognized_numbers = ''.join(filter(str.isdigit, numbers))
    print(recognized_numbers)

    # 화면에 인식된 숫자 출력
    cv2.putText(image, recognized_numbers, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Number Recognition', image)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # raw_capture 버퍼 지우기
    raw_capture.truncate(0)

# 종료 시 카메라와 창 해제
camera.close()
cv2.destroyAllWindows()
