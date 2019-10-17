import NtKinect
import cv2

while(1):
    NtKinect.setRGB()
    NtKinect.setSkeleton()
    NtKinect.setFace()
    NtKinect.imshowBlack()

    if cv2.waitKey(25) & 0xFF == ord('q'):
        NtKinect.stopKinect()
        break
