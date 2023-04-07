# Robot Football

Hello all! This is a walk-through for the Bachelor Thesis Robot Football (2022/23) at Trinity College Dublin by Melissa Mazura. 

This project can detect a hand (palm up, hand out) and three different coloured balls. After detecting these obejcts, there are two different commands the robot can perform. If one hand is found in the image, it will turn 360°. When there is one ball, the robot will follow its path and "catch" the ball. 

Do you want to test it?

You can also add your own images into the mix! If you are up to that, simply keep reading till the end. Make sure you follow each step that is described here and if you need help, please don't hesitate to ask for help from me or Conor Sheedy. 

Have fun!

# How to run the code:

## 1. Requirements

### The Robot

The robot can be found in this link: https://www.elegoo.com/products/elegoo-smart-robot-car-kit-v-4-0. 

The robot's assembly can be accomplished by using the eTutorial provided by Elegoo. The robot has a camera module, a remote control and an infra red sensor. The averate time of putting it together is 2 hours. Make sure to accomplish every step after the other and to tighten the screws as good as possible. In the end, the robot should look like this:

<img src="https://user-images.githubusercontent.com/115803011/220768214-73aa3c63-2037-41fb-baa9-8641828a3d82.jpg" width="50%">

### The Balls

The other requirement are three balls from Amazon. The Object Detection algorithm is designed to detect those three balls. There is no guarantee that the algorithm works on any other balls. 

### Other requirements

You have to have Python 3.10 or lower. If you have a newer version, please downgrade. The detection will not work with a higher version.

Go to https://github.com/WongKinYiu/yolov7 and download the repository. Then, download the files from here and go move everything into the yolov7 repository. 

When you have done this, open the terminal and move into the yolov7 repository. Run pip install -r /Robot_Football/requirements.txt. Also run pip install pyserial and pip install opencv-python. 

While you are downloading everything necessary, open up the utils/google_utils.py. Change line 31 to tag = “v1.0”.

When you have done that, go into the https://www.elegoo.com/blogs/arduino-projects/elegoo-smart-robot-car-kit-v4-0-tutorial and download the first link. There, you have go to  02 Manual & Main Code & APP\02 Main Program\TB6612 & QMI8658C\SmartRobotCar and switch out the ApplicationFunctionSet_xxx0.cpp with the one given in the GitHub repository.

Make sure that all these requirements are fullfilled.

## 2. The robot

After you have assembled the robot, the next step is updating the code of said robot. For this, open the modified 02 Manual & Main Code & APP\02 Main Program\TB6612 & QMI8658C\SmartRobotCar folder in the Arduino IDE and coonect your robot with the USB cable. Connect it with the board Arduino UNO and the Port COM6. Then, please upload the new code to the robot.

## 3. Object Detection

Please ask Conor for the weight files. 

You are almost ready for the object detection. Please connect your computer to the Wifi of the robot. To see whether the connection works, go to http://192.168.4.1. When this works, make sure that the USB is still connected to the robot, set it on the ground and close the Arduino IDE. When this is done, run the following line from your yolov7 repository (with my code in it as well!):

python det_run.py --weights SPECIFY WEIGHT HERE.pt --conf 0.5 --img-size 640 --source "http://192.168.4.1/capture"

<img src="https://user-images.githubusercontent.com/115803011/220776390-ade5ad59-5315-408f-9f4f-e163efbefa74.jpg" width="50%">

This is what the detection should look like.

# HOW TO CREATE YOUR OWN MODEL:

## 1. The Dataset

### Take images

You can add your own object detection module to the mix. Just think of an object you want to use, download take_photo.py to your local machine and make sure to follow the instructions at all the right places. Then run the code. You should take at least 50 images per class. This way you will take many pictures with openCV in a row, so have all the objects ready! Make sure that the object is well photographed and afterwards go through the pictures to make sure it actually works.

<img src="https://user-images.githubusercontent.com/115803011/220775344-13053b29-fc2f-4c17-b20c-f01b229a0c69.png" width="50%">

### Label images

After this, download labelImg from github (https://github.com/heartexlabs/labelImg). You can start it by typing python labelImg.py or if on windows the_path_to_file python labelImg.py. Change the (1) open and (2) save directory to the one with the images and then change the (3) save format to Yolo. Then create boxes (they are called bounding boxes) with the (4) CreateRec to circle the objects. Hit ctlr + w to faciliate the creation of bounding boxes. When every image is annotated, close labelImg and you are done! 

### Run Augmentation

Open up the data_augmentation notebook and open it. YOu have to upload your image folder into google drive. Then, simply connect to Google Drive in the notebook and specify the path. Then, run it!

## 2. Train your own onject detection algorithm

All instructions for this part are in the run_train jupyter notebook. So, relax and work through it!

## 3. Run it

Wow, you have officially created your custom detection module! Now, you can have some fun with it! 

Run the next line with your own weights:

python det_run.py --weights SPECIFY WEIGHT HERE.pt --conf 0.5 --img-size 640 --source "http://192.168.4.1/capture"


