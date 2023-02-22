import cv2
import os
import time

if not os.path.exists('dataset'):
    os.mkdir('dataset')
labels = ['ball', 'hand', 'both']
vid_capture = cv2.VideoCapture(0)
if not vid_capture.isOpened():
    print("cannot open camera")
for label in labels:
    if not os.path.exists(f'dataset/{label}'):
        os.mkdir(f'dataset/{label}')
        print(f"{label} directory created")
    print(f"Take pictures for {label} in 5 seconds...")
    label_path = f"dataset/{label}"
    time.sleep(4)
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
            i += 1
            cv2.imwrite(label_path + f"/{label}{52 + i}.jpg", frame)
            if i >= 50:
                break
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

vid_capture.release()
cv2.destroyAllWindows