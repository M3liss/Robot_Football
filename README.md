# Robot Football

This is a walk-through for the Bachelor Thesis Robot Football (2022/23) in Trinity College Dublin by Melissa Mazura. 

If you do not want to add your own dataset, please jump ahead after 1. Requiremnets to step 4. Connection to the Robot. There is no rush to start with your own detection before making sure you understand the rest of it!

# 1. Requirements

## The Robot

The robot can be found in this link: https://www.elegoo.com/products/elegoo-smart-robot-car-kit-v-4-0. 

The robot's assembly can be accomplished by using th eTutorial provided by Elegoo. It has a camera module, a remote control and an infra red sensor. The averate time of putting it together is 2 hours. Make sure to accomplish every step after the other. In the end, the robot should look like this:
![photo_2023-02-22_16-52-13](https://user-images.githubusercontent.com/115803011/220768214-73aa3c63-2037-41fb-baa9-8641828a3d82.jpg)

## The Balls

The other requirement are three balls from Amazon. The Object Detection algorithm is designed to detect those three balls. There is no guarantee that the algorithm works on any other balls. 

## The requirements

Make sure to download the requirements.txt file and run !pip install -r /Robot_Football/requirements.txt

# 2. The Dataset

You can add your own object detection module to the mix. Just think of an object you want to use, download take_photo.py to your local machine and make sure to follow the instructions at all the right places. Then run the code. This way you will take NUMBER pictures with openCV in a row, so have all the objects ready! Make sure that the object is well photographed and afterwards go through the pictures to make sure it actually works.

![annotated_labelImg](https://user-images.githubusercontent.com/115803011/220775344-13053b29-fc2f-4c17-b20c-f01b229a0c69.png)
After this, download labelImg from github (https://github.com/heartexlabs/labelImg). You can start it by typing python labelImg.py or if on windows the_path_to_file python labelImg.py. Change the (1) open and (2) save directory to the one with the images and then change the (3) save format to Yolo. Then create boxes (they are called bounding boxes) with the (4) CreateRec to circle the objects. Hit ctlr + w to faciliate the creation of bounding boxes. When every image is annotated, close labelImg and you are done! 


Make sure to find the classes.txt file and copy the classes from it. Then, go to the images folder in your google drive, upload your own images and add your class to the classes.txt file that already exists.

# 3. Object Detection

Wow, you have officially added your own images! Now, you can have some fun with it! Open the jupyter notebook yolov7_det.ipynb and go through the steps speficied. If you need help, go to the official yolov7 repository on GitHub to find information. Have fun with this and make sure you use the free GPU in Google Colab as much as you can to improve your detection algorithm.

# 4. Connection to the robot

Awesome, you are almost done! The next step is to actually connect to the robot and run your new algorithm!
