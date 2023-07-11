import cv2
import pytesseract

# 이미지에서 숫자를 인식하는 함수
def recognize_numbers(image):
    # 이미지를 그레이스케일로 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 이미지에서 숫자를 인식
    numbers = pytesseract.image_to_string(gray, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

    return numbers

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    # 숫자 인식
    numbers = recognize_numbers(frame)

    # 숫자만 추출하여 출력
    recognized_numbers = ''.join(filter(str.isdigit, numbers))
    print(recognized_numbers)

    # 화면에 인식된 숫자 출력
    cv2.putText(frame, recognized_numbers, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Number Recognition', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료 시 비디오 캡처 객체와 창 해제
cap.release()
cv2.destroyAllWindows()
