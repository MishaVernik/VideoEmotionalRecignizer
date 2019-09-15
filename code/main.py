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
    face = 0
    print(rects)
    for (i, rect) in enumerate(rects):
        # Make the prediction and transfom it to numpy array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        top = 99999;
        bot = 0;
        left = 99999
        right = 0
        for (x, y) in shape:
            top = min(y,top)
            bot = max(y,bot)
            left = min(x,left)
            right = max(x,right)

        right += 20
        left -= 20
        top -=20
        bot +=20

        while (right-left) / (bot-top) > 3/4:
            top -= 1
            bot +=1

        cv2.rectangle(image,(left,top),(right,bot),(255,0,0),2)

        # Draw on our image, all the found cordinate points (x,y)
        for (x, y) in shape:
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)

            #cv2.rectangle(image, (x, y), (end_cord_x_width, end_cord_y_height), color, stroke)

        face = image[top:bot, left:right]


        # Show the image
        cv2.imshow("Output", face)
        cv2.imwrite("data/" + str(cnt) + ".png", face)
        w = right - left;
        h = bot - top
        with open("data/"+ str(cnt) + ".txt","w") as o:
            for (x, y) in shape:
                o.write(str(((x-left) / w))+" "+str(((y - top) / h))+"\n")



    cnt += 1
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
