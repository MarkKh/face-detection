import cv2
imagePath = r'bts.jpg'
cascPath = "haarcascade_frontalface_default.xml"
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier(cascPath)
faces = faceCascade.detectMultiScale(gray)
print(f'There are {len(faces)} faces found.')
for (x, y, w, h) in range(len(faces(0,1))):
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    if faces == 2:
        break
cv2.imshow("Faces found", image)
cv2.waitKey(0)
