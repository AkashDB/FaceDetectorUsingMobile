import cv2, time

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("smile.xml")

# For Webcam use only this
# video = cv2.VideoCapture(0)

# for mobile as a webcam use this with mobile application IP Webcam.
video = cv2.VideoCapture(0)
address = "https://192.168.0.100:8080/video"
video.open(address)

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in face:
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Got it", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

# without mobile

    # import cv2, time
    #
    # face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # smile_cascade = cv2.CascadeClassifier("smile.xml")
    #
    # video = cv2.VideoCapture(0)
    #
    # while True:
    #     check, frame = video.read()
    #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    #
    #     for (x, y, w, h) in face:
    #         img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #
    #         smile = smile_cascade.detectMultiScale(gray, scaleFactor=1.8, minNeighbors=10)
    #         for (x, y, w, h) in smile:
    #             img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #
    #     cv2.imshow("Got it", frame)
    #     key = cv2.waitKey(0)
    #
    #     if key == ord('q'):
    #         break
    #
    # video.release()
    # cv2.destroyAllWindows()

