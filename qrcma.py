import cv2
from pyzbar import pyzbar
import serial

# 시리얼 통신 설정
serial_port = 'COM3'  # 시리얼 포트를 적절한 값으로 변경해주세요.
baud_rate = 9600  # 시리얼 통신 속도를 적절한 값으로 변경해주세요.
ser = serial.Serial(serial_port, baud_rate)

# 웹캠으로부터 영상 캡처
cap = cv2.VideoCapture(0)  # 웹캠 인덱스를 적절한 값으로 변경해주세요.

# 인식할 큐알 코드 유형 설정
allowed_formats = ['QRCODE', 'CODE128', 'EAN13']  # 인식할 큐알 코드 유형을 적절히 선택해주세요.

while True:
    # 영상 캡처
    ret, frame = cap.read()

    # QR 코드 인식
    barcodes =pyzbar.decode(frame)

    for barcode in barcodes:
        barcode_type = barcode.type

        # 인식할 큐알 코드 유형인지 확인
        if barcode_type in allowed_formats:
            # QR 코드의 내용 추출
            qr_code_data = barcode.data.decode("utf-8")
            print("인식된 큐알 코드 유형:", barcode_type)
            print("인식된 코드 내용:", qr_code_data)
            if (qr_code_data == 'https://www.qrfy.com/SFwfttXhbi'):
                ser.write('1'.encode())

            # 시리얼 통신을 통해 데이터 전송
            

    # 화면에 영상 출력
    cv2.imshow("QR Code Scanner", frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 리소스 해제
cap.release()
cv2.destroyAllWindows()
ser.close()
