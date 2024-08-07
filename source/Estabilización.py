from sense_hat import SenseHat
import time
import RPi.GPIO as GPIO

# Inicializa SenseHAT
sense = SenseHat()

# Configuración de los pines GPIO para los servos
steering_servo_pin = 17  # Pin GPIO para el servo de dirección
throttle_servo_pin = 18  # Pin GPIO para el servo de aceleración

GPIO.setmode(GPIO.BCM)
GPIO.setup(steering_servo_pin, GPIO.OUT)
GPIO.setup(throttle_servo_pin, GPIO.OUT)

# Configuración de los servos (frecuencia PWM)
steering_servo = GPIO.PWM(steering_servo_pin, 50)  # Frecuencia de 50Hz
throttle_servo = GPIO.PWM(throttle_servo_pin, 50)  # Frecuencia de 50Hz

# Inicializa los servos
steering_servo.start(7.5)  # Posición neutral (90 grados)
throttle_servo.start(7.5)  # Posición neutral (90 grados)

# Parámetros PID
Kp = 1
