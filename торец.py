import cv2

path = "f:\\Trassir\\screenshots\\"
cap = cv2.VideoCapture("rtsp://admin:Energoadmin555@172.18.19.17:554/cam/realmonitor?channel=1&subtype=0")


i = 0
j = 1
while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    f = path + "\\" + "image" + str(i).zfill(6) + '.jpg'
    # в имени файла добавляем нули - у ffmpeg проблемы с шаблонами под виндой
    cv2.imwrite(f, frame)

    i = i + 1
    j = j + 30
    #каждый 30-й кадр
    cap.set(1, j)


cap.release()
cv2.destroyAllWindows()