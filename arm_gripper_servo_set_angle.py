from picobot_arm import PicoBotArm
import time

# Граници за безопасна работа на серво канала за щипката (канал 2)
# НЕ ПРОМЕНЯЙТЕ тези стойности, освен ако сте напълно сигурни!
MIN_CLAW_ANGLE = 40
MAX_CLAW_ANGLE = 140

# Желан ъгъл за тестване
desired_angle = 50

# Гарантираме, че ъгълът е в безопасни граници
safe_angle = max(MIN_CLAW_ANGLE, min(MAX_CLAW_ANGLE, desired_angle))

arm = PicoBotArm(init_servos=False)

# Задаваме ъгъла на сервомотора за щипката (канал 2)
arm.control_servo(channel=2, angle=safe_angle)

time.sleep(2)
