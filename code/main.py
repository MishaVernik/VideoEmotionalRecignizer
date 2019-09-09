from imutils import face_utils
import dlib
import cv2

# Vamos inicializar um detector de faces (HOG) para então
# let's go code an faces detector(HOG) and after detect the
# landmarks on this detected face

face_cascade = cv2.CascadeClassifier('venv/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
# p = our pre-treined model directory, on my case, it's on the same script's diretory.
p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

cap = cv2.VideoCapture(0)
cnt = 0
while True:
    # Getting out image bx y webcam
    _, image = cap.read()
    # Converting the image to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Get faces into webcam's image
    rects = detector(gray, 0)

    # For each detected face, find the landmark.
    for (i, rect) in enumerate(rects):
        # Make the prediction and transfom it to numpy array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # Draw on our image, all the found cordinate points (x,y)
        for (x, y) in shape:
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            print(x, y, w, h)
            #   capture your face
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = image[y:y + h, x:x + w]  # (y, y + h)

            cv2.imwrite("data/frame/" + str(cnt) + ".png", roi_gray)
            cnt += 1
            if cnt >5:
                cnt  = 0;
                break

            color = (255, 0, 0)  # BGR

            stroke = 2
            end_cord_x_width = x + w
            end_cord_y_height = y + h
            cv2.rectangle(image, (x, y), (end_cord_x_width, end_cord_y_height), color, stroke)

    # Show the image
    cv2.imshow("Output", image)

    cv2.imwrite("data/" + str(cnt) + ".png", image)

    cnt += 1
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()