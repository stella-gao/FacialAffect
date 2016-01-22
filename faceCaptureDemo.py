import cv2

'''
Todo: implement optical flow tracking method later on...
'''

'''
Implement this face capture as a function in which you can pass
the model as a parameter and it would return to you can image.

Then we can have a fallback image in the event that shit just
goes wrong and it would be for a more robust tracking experience
'''
def get_dimensions(lena, face_classifier):
    face = face_classifier.detectMultiScale(lena, 1.3, 5)
    x = 0
    y = 0
    width = 0
    height = 0

    if len(face) is 1:
        for (x,y,width,height) in face:
            lena_small = lena[y: y+height, x: x+width]
            return lena_small, x, y, width, height
    else:
        return None

# Import Haarcascade Dataset
#face_classifier = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
face_classifier = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)
ret, prev = cap.read()

try:
    prev_small, x, y, width, height = get_dimensions(frame, face_classifier)
except:
    pass

while True:
  ret, frame = cap.read()
  cv2.imshow('Webcam Image', frame)

  try:
      lena_small, x, y, width, height = get_dimensions(frame, face_classifier)
      if lena_small is not None:
          cv2.imshow('Cropped Face Region', lena_small)
  except:
      pass

  if cv2.waitKey(1) & 0xFF==ord('q'):
      break
