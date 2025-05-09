from picobot_arm import PicoBotArm
import time

# Граници за безопасна работа на серво канала за основата (канал 0)
# НЕ ПРОМЕНЯЙТЕ тези стойности, освен ако сте напълно сигурни!
MIN_BASE_ANGLE = 0
MAX_BASE_ANGLE = 180

# Желан ъгъл за тестване
desired_angle = 90

# Гарантираме, че ъгълът е в безопасни граници
safe_angle = max(MIN_BASE_ANGLE, min(MAX_BASE_ANGLE, desired_angle))

# Създаване на обект за управление на сервомоторите без автоматично позициониране
arm = PicoBotArm(init_servos=False)

# Задаване на ъгъл на сервото за основа (канал 0)
arm.control_servo(channel=0, angle=safe_angle)

time.sleep(2)

