from picobot_arm import PicoBotArm
import time

# Граници за безопасна работа на серво канала за рамото (канал 1)
# НЕ ПРОМЕНЯЙТЕ тези стойности, освен ако сте напълно сигурни!
MIN_ARM_ANGLE = 40
MAX_ARM_ANGLE = 140

# Желан ъгъл за тестване
desired_angle = 90

# Гарантираме, че ъгълът е в безопасни граници
safe_angle = max(MIN_ARM_ANGLE, min(MAX_ARM_ANGLE, desired_angle))

arm = PicoBotArm(init_servos=False)

# Задаваме ъгъла на сервомотора за рамото (канал 1)
arm.control_servo(channel=1, angle=safe_angle)

time.sleep(2)
