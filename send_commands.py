import serial 
import time
class connectCar:
    def __init__(self, port):
        try:
            self.car = serial.Serial(port, 9600)
            print(f"Connection on {port}")
            self.is_connect = 1
        except:
            self.is_connect = 0
    
    def check_connection(self):
        return(self.is_connect)
    
    def turn_360(self):
        self.car.write("360".encode())

    def follow_ball(self, x1):
        MAX_SPEED = 100
        speedA, speedB = 0, 0
        if (x1 < 0.5):
            speedA = x1 * 2 
            speedA = MAX_SPEED * speedA
            speedB = MAX_SPEED
        if (x1 > 0.5):
            speedA = MAX_SPEED
            speedB = (x1 - 0.5) * 2
            speedB = MAX_SPEED * speedB
            speedB = MAX_SPEED - speedB
        if (x1 == 0.5):
            speedA, speedB = MAX_SPEED, MAX_SPEED
        speedA = int(round(speedA, 0))
        speedB = int(round(speedB, 0))
        print(f"for {x1} SpeedA = {speedA} and SpeedB = {speedB}")
        self.car.write(f"{speedA}:{speedB}".encode())
    def stop(self):
        self.car.write("STOP".encode())

