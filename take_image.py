import cv2
import os
import time

# TO DO
# add the labels to the path. You can either add all the labels at once (it will take all the pictures after one another) or type in one label after the other. 
labels = ['', '', '']

# TO DO
# add the path for where the pictures should be saved.
path = ""
if not os.path.exists(path):
    os.mkdir(path)
vid_capture = cv2.VideoCapture(0)
if not vid_capture.isOpened():
    print("cannot open camera")
for label in labels:
    print(f"Take pictures for {label} in 5 seconds...")
    label_path = f"{path}/{label}"
    time.sleep(2)
    start = time.time()
    i = 0
    while True:
        #capture frame by frame
        ret, frame = vid_capture.read()
        if not ret:
            print("Cannot receive frame. Make sure no other application is using the camera.")
            break
        cv2.imshow('openCV Feed', frame)
        if time.time() - start > 2:
            print(f"Take picture {i}th")
            start = time.time()
            cv2.imwrite(label_path + f"/{label}{i}.jpg", frame)
            i += 1
            if i > 50:
                break
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

vid_capture.release()
cv2.destroyAllWindows
