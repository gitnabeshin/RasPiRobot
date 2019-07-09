import time
import RPi.GPIO as GPIO
# GPIOのモードをセット（GPIO番号で指定）
GPIO.setmode(GPIO.BCM)

import motor
import sensor
import servo
import sound
import led

KYORI=15

# ロボットを初期化する
def init():
	# モータ停止
	motor.stop()
	sound.STARTUP()
	led.STARTUP()
	# 顔を正面に向ける
	servo.drive_servo(servo.FRONT)

# メインプログラム
def start_main():
	init()
	print("init")
	
	while True:
		# 距離が15cm以上だったら1秒間前に進む
		print("while")
		if sensor.getDistance() >=KYORI:
			motor.drive(motor.FORWARD)
			print("GO Forward")
			sound.CLOCK()
			led.blue_blink(0.8)
			time.sleep(0.5)
		# 距離が5cm以下だったら止まって、方向転換
		else:  #sensor.getDistance() <= KYORI:
			sound.NG()
			motor.stop()
			led.red_blink(0.8)
			# 左を確認
			servo.drive_servo(servo.LEFT)
			# 距離が6cm以上だったら方向転換
			if sensor.getDistance() >= KYORI:
				sound.OK()
				led.blue_blink(0.8)
				motor.drive(motor.TURN_LEFT)
				print("TURN LEFT")
				led.seq_back(3)
				time.sleep(1)
				servo.drive_servo(servo.FRONT)
				######=================----------------------------------------------------------
			else:
				sound.NG()
				led.red_blink(0.8)
				# 右を確認
				servo.drive_servo(servo.RIGHT)
				# 距離が6cm以上だったら方向転換
				if sensor.getDistance() >= KYORI:
					sound.OK()
					led.blue_blink(0.8)
					motor.drive(motor.TURN_RIGHT)
					print("TURN RIGHT")
					led.seq_forward(3)
					time.sleep(1)
					servo.drive_servo(servo.FRONT)
				# もう進めない場合は後ろに下がって回れ右
				else:
					sound.NG()
					led.red()
					print("led.red")
					motor.drive(motor.BACKWARD)
					print("motor.drive")
					time.sleep(2)
					servo.drive_servo(servo.FRONT)
					# End
					if sensor.getDistance() <= KYORI:
						sound.END()
						motor.end()	
						led.seq_forward(1.2)
						led.seq_back(1.2)
						time.sleep(1)
						servo.drive_servo(servo.RIGHT)
						servo.drive_servo(servo.LEFT)
						servo.drive_servo(servo.RIGHT)
						servo.drive_servo(servo.FRONT)
						sensor.end()
						servo.end()
						GPIO.cleanup()
					else:
						sound.OK()
						motor.drive(motor.TURN_RIGHT)
						time.sleep(1)

try:
	#ここからスタート
	start_main()
except KeyboardInterrupt:
	#全体の終了
	motor.end()
	sensor.end()
	servo.end()
	sound.END()
	GPIO.cleanup()
