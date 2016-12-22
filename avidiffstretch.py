import cv2
import numpy as np

stream = cv2.VideoCapture(r"c:\tmp\hbcropped.avi")
if stream.isOpened() == False:
    print ("Cannot open input video!")

prvgrey=None
cumul = None

while True:

    _ ,frame = stream.read()
    framegray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY) #1 pour 1 plan rgb
    height, width = framegray.shape
    dst = np.zeros(shape=(height, width))
    if cumul is None:
        cumul = np.zeros(shape=(height, width), dtype=np.float64)

    if prvgrey is not None:
        diff = cv2.absdiff(framegray,prvgrey)
        fdiff = diff.astype('float64') #cast en flaot car cv2.add marche entre flaota

        cumul = cv2.addWeighted(cumul,0.998,fdiff,0.002,0) #gere les depassements alors que + ne le fait pas
        #cumul = cv2.add(cumul, fdiff)  # il faut des flaot gere les depassements alors que + ne le fait pas
        #divvmul = cv2.equalizeHist(diff)

        cv2.imshow('truc',cumul)
        ch = 0xFF & cv2.waitKey(1)  # Wait for a second
        if ch == 27:
            break

    prvgrey = framegray

cv2.destroyAllWindows()
