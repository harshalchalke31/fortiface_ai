import cv2
import uuid
import os
from prepare_data import anc_path,pos_path
print(os.getcwd())
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame = cap.read()
    # resize image to 250x250
    frame = cv2.resize(frame,(250,250))

    # Collecting anchor images
    if cv2.waitKey(1) & 0xFF==ord('a'):
        # create unique file path
        imgname= os.path.join(fr"{os.getcwd()}\data\anc",'{}.jpg'.format(uuid.uuid1()))
        print(imgname)
        # write out anchor image
        cv2.imwrite(imgname,frame)

    # Collecting positive images
    if cv2.waitKey(1) & 0xFF==ord('p'):
        # create unique file path
        imgname= os.path.join(f"{os.getcwd()}\data\pos",'{}.jpg'.format(uuid.uuid1()))
        print(imgname)
        # write out anchor image
        cv2.imwrite(imgname,frame)
    cv2.imshow('Dataset Collection',frame)
    # Break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the webcam
cap.release()
# close the image show frame
cv2.destroyAllWindows()
