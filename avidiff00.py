import numpy as np
import cv2

#une autre mouture de avidiffstretch un peu differente
#avec d'autre fonctions mais le resultat est tres voisin
cap = cv2.VideoCapture(r"c:\tmp\hbcropped.avi")

lstframe = None
cumul = None

grandcumul=None

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    #cv2.imshow('frame',frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    #fframe = frame.astype(float)

    delta  =None
    if not lstframe is None:
        delta = cv2.subtract(hsv,lstframe)

    lstframe = hsv.copy()

    if delta is None:
        continue

    height = np.size(hsv, 0)
    width = np.size(hsv, 1)

    #dbblur = np.array((height,width),np.uint8)
  #  dbblur = cv2.blur(delta, (3,3))
    #th, dst = cv2.threshold(abs(delta), 0, 255, cv2.THRESH_BINARY);

  #  if cumul == None:
  #      cumul = abs(dbblur).astype(float)
  #  else:
  #      cumul = abs(dbblur).astype(float)*.2+cumul*.8


    if grandcumul is None:
        grandcumul = abs(delta).astype(float)
    else:
        grandcumul = grandcumul *.98 + abs(delta).astype(float)*.02


    cumul2 = np.zeros((height, width), np.uint8)
    b =cv2.normalize(grandcumul, cumul2, 0, 256, cv2.NORM_MINMAX);

    #roi_red = cv2.bitwise_and()
    if not delta is None:
        cv2.imshow('frame', grandcumul)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()