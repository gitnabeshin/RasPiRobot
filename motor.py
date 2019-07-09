import time
import RPi.GPIO as GPIO
# GPIOのモードをセット（GPIO番号で指定）
GPIO.setmode(GPIO.BCM)

#GPIOのポートを指定
# 左のモーター用
PIN_R1 = 2						#3pin
PIN_R2 = 3						#5pin
# 右のモーター用
PIN_L1 = 17					#11pin
PIN_L2 = 27					#13pin
# モーター速度制御用
PIN_DUTY = 4				#7pin

# モータの動き
STOP = 0
FORWARD = 1
BACKWARD = 2
TURN_RIGHT = 3
TURN_LEFT = 4
# モータ番号
RIGHT = 0
LEFT = 1

# モーターのポート分GPIOの出力用に指定
GPIO.setup(PIN_R1, GPIO.OUT)
GPIO.setup(PIN_R2, GPIO.OUT)
GPIO.setup(PIN_L1, GPIO.OUT)
GPIO.setup(PIN_L2, GPIO.OUT)
GPIO.setup(PIN_DUTY, GPIO.OUT)

# モータの回転速度を指定
pwm_LR = GPIO.PWM(PIN_DUTY, 30)
pwm_LR.start(100)

# モーターを制御する関数
# @param motor_no = LEFT/RIGHT
# @param act = FORWARD/BACKWARD/STOP
def set_motor(motor_no, act):
	# 右のモーターが指定された場合
	if motor_no == RIGHT:
		# 前回転
		GPIO.output(PIN_R1, 1)
		GPIO.output(PIN_R2, 0)
		# 後回転
		if act == BACKWARD :
			GPIO.output(PIN_R1, 0)
			GPIO.output(PIN_R2, 1)
		# STOP
		if act == STOP :
			GPIO.output(PIN_R1, 0)
			GPIO.output(PIN_R2, 0)
	# 左のモーターが指定された場合
	elif motor_no == LEFT:
		# 前回転
		GPIO.output(PIN_L1, 1)
		GPIO.output(PIN_L2, 0)
		# 後回転
		if act == BACKWARD :
			GPIO.output(PIN_L1, 0)
			GPIO.output(PIN_L2, 1)
		# STOP
		if act == STOP :
			GPIO.output(PIN_L1, 0)
			GPIO.output(PIN_L2, 0)
	else:
		print ("ERROR invalid motor NO.")

# 両方のモーターを同時に制御する
# @param act = FORWARD/BACKWARD/TURN_RIGHT/TURN_LEFT/STOP
def drive(act):
	print ("move [", act , "] / FORWARD[1]/BACKWARD[2]/TURN_RIGHT[3]/TURN_LEFT[4]/STOP[0]")
	if act == TURN_RIGHT:
		set_motor(RIGHT, BACKWARD) 
		set_motor(LEFT, FORWARD) 
	elif act == TURN_LEFT:
		set_motor(RIGHT, FORWARD)
		set_motor(LEFT, BACKWARD) 
	else:  
		set_motor(RIGHT, act) # 左
		set_motor(LEFT, act) # 右

# 両方のモーターをストップする
def stop():
	set_motor(RIGHT, STOP) 
	set_motor(LEFT, STOP )

def end():
	pwm_LR.stop()
	print ("motor end.")

# このプログラムファイルで動作確認
if  __name__ ==  "__main__":
	try:
		while True:
			drive(FORWARD) # 前へ
			time.sleep(3)
			drive(BACKWARD) # 後ろへ
			time.sleep(3)
			drive(TURN_RIGHT) # 右へ
			time.sleep(3)
			drive(TURN_LEFT) # 左へ
			time.sleep(3)
			stop() # 停止
			time.sleep(3)

	except KeyboardInterrupt:
		end()
		GPIO.cleanup()
