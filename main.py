import numpy as np
import cv2
import random

very_important_int = 0
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
xout = 1000
yout = 1000
cap = cv2.VideoCapture(0)
ToBeTrueOrNotToBeTrue = 0
width = cap.get(3)
height = cap.get(4)


def kostil(useless):
    nchars = len(useless)
    x = sum(ord(useless[byte]) << 8 * (nchars - byte - 1) for byte in range(nchars))
    return x


max_people = int(input('Введите максимально возможное число человек:' + '\n'))

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return_value, image = cap.read()
    # if format(len(faces)) == "1":
    #     ToBeTrueOrNotToBeTrue = 1
    # elif format(len(faces)) == "0":
    #     ToBeTrueOrNotToBeTrue = 1
    # else:
    #     ToBeTrueOrNotToBeTrue = 0
    xx = -1
    yy = -1
    for (x, y, w, h) in faces:
        very_important_int = random.randint(1, 4)
        xx = x
        yy = y
        x1 = 0
        x2 = 0
        if int(format(len(faces))) > max_people:
            print(
                f'ВНИМАНИЕ, В ПОМЕЩЕНИИ НАХОДЯТСЯ {format(len(faces))} ЧЕЛОВЕК, ЭТУ ПРЕВЫШАЕТ НОРМУ НА {int(format(len(faces))) - max_people} ЧЕЛОВЕК')
        else:
            print('кол-во лиц:', format(len(faces)))
        # if ToBeTrueOrNotToBeTrue == 1:
        xpos = ((x + w / 2) - width / 2)
        ypos = ((y + h / 2) - height / 2)
        xout = round(np.clip(xout + -5 * (xpos / abs(xpos / 2) if (abs(ypos) > width / 20) else 0), 0, 2000))
        yout = round(np.clip(yout + 5 * (ypos / abs(ypos / 2) if (abs(ypos) > height / 20) else 0), 0, 2000))
        cv2.circle(img, (x + w // 2, y + h // 2), (w // 2), (0, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
    img = cv2.resize(img, (0, 0), fx=3, fy=1.5)
    cv2.imshow('img', img)
    # kek = cv2.IMREAD_COLOR(img, -1)
    # cv2.imshow('img', kek)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
