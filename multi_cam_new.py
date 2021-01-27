import cv2
import numpy as np
from matplotlib import pyplot as plt
ret = []
frame = []
retframtup = []
nstart = 0
ncam = 1
cam = []

ctemp = np.zeros([256, 256])

for i in range(nstart,nstart+ncam):

    cam.append(cv2.VideoCapture(i))


while(True):

    for i in range(0, ncam):

        strname = "cam_{}".format(str(i))

        if list(cam[i].read())[0] == False:

            cv2.imshow("feed_unavailable", ctemp)


        else:
            cv2.imshow(strname, list(cam[i].read())[1])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


for i in range(0, ncam):
    cam[i].release()

cv2.destroyAllWindows()
