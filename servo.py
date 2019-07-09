import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

PIN_SERVO = 22		#15pin
GPIO.setup(PIN_SERVO, GPIO.OUT)

# 20ms
frameTime = 20
# 50Hz
freq = 1000 / frameTime

RIGHT = 0
LEFT = 1
FRONT = 2

pwm_SERVO = GPIO.PWM(PIN_SERVO, freq)
pwm_SERVO.start(0)

# @param direction = LEFT/RIGHT/FRONT
def drive_servo( direction ):
		if direction == LEFT:
			pulseWidth = 2.30 
			print ("look left")
		elif direction == RIGHT:
			pulseWidth = 0.75
			print ("look right")
		elif direction == FRONT:
			pulseWidth = 1.5
			print ("look front")
		else:
			print ("ERROR illegal direction.")
		pwm_SERVO.ChangeDutyCycle( 100 * pulseWidth / frameTime )
		time.sleep(0.6)

def end():
	pwm_SERVO.stop()
	print ("servo end.")

# このプログラムファイルで動作確認
if  __name__ ==  "__main__":
	try:
		while True:
			drive_servo(LEFT)
			drive_servo(FRONT)
			drive_servo(RIGHT)
			drive_servo(FRONT)

	except KeyboardInterrupt:
		end()
		GPIO.cleanup()


