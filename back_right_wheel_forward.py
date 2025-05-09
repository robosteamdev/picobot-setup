from picobot_motors import MotorDriver
import time

motors = MotorDriver()

motors.TurnMotor("RightBack", "forward", speed=80) #speed = 0 до 100
time.sleep(2)
motors.MotorStop("RightBack")
