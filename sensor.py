import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIN_TRIG = 10			#19pin
PIN_ECHO = 9			#21pin
GPIO.setup(PIN_TRIG,GPIO.OUT)
GPIO.setup(PIN_ECHO,GPIO.IN)

# 距離センサの値を返す
def readSignal():

		GPIO.output(PIN_TRIG, GPIO.LOW)
		time.sleep(0.3)

		GPIO.output(PIN_TRIG, True)
		time.sleep(0.00001)
		GPIO.output(PIN_TRIG, False)
 
		#初期化
		signaloff = 0
		signalon = 0
 
		while GPIO.input(PIN_ECHO) == 0:
			signaloff = time.time()
         
		while GPIO.input(PIN_ECHO) == 1:
			signalon = time.time()
 
		timepassed = signalon - signaloff
		distance = timepassed * 17000
		return distance

# 距離センサの計測値３回の平均を返す
def getDistance():
	data1 = readSignal()
	time.sleep(0.01)
	data2 = readSignal()
	time.sleep(0.01)
	data3 = readSignal()

	# 3回の平均を計算する
	return (data1 + data2 + data3 ) / 3 

def end():
	print ("sensor end.")

# このプログラムファイルで動作確認
if  __name__ ==  "__main__":
	
	print("START")
	
	try:
		while True:
			print ( "distance = [", getDistance() , "]")
			time.sleep(0.2)

	except KeyboardInterrupt:
		end()
		GPIO.cleanup()
