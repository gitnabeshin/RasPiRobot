# coding: utf-8
import RPi.GPIO as GPIO
import time

SOUNDER = 21 #Pin40/BOARD, GPIO21/BCM
#DOREMI_Hz = [ 262, 294, 330, 349, 392, 440, 494, 523 ]
OK_Hz=392
NG_Hz=180
CLOCK_Hz=440
END_Hz=650

GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUNDER, GPIO.OUT) 

freq=440
p = GPIO.PWM(SOUNDER, freq)
p.start(50)

def OK():
		print ("supi-ka-.OK." )
		#p.ChangeFrequency(OK_Hz)
		#time.sleep(1)
		p.start(50)
		p.ChangeFrequency(620)
		time.sleep(0.1)
		p.ChangeFrequency(700)
		time.sleep(0.2)
		p.stop()
		time.sleep(1)
		
		
def NG():
		print ("supi-ka-.NG.")
		#p.ChangeFrequency(NG_Hz)
		#time.sleep(1)
		p.start(50)
		p.ChangeFrequency(180)
		time.sleep(0.1)
		p.ChangeFrequency(120)
		time.sleep(0.2)
		p.stop()
		time.sleep(1)


def CLOCK():
		print ("supii-ka-.CROCK.")
		#p.ChangeFrequency(CLOCK_Hz)
		#time.sleep(1)
		p.start(50)
		p.ChangeFrequency(390)
		time.sleep(0.2)
		p.ChangeFrequency(440)
		time.sleep(0.2)
		p.stop()
		time.sleep(1)

	
def END():
		print ("supi-ka-.END.")
		#p.ChangeFrequency(END_Hz)
		#time.sleep(1)
		p.start(50)
		p.ChangeFrequency(390)
		time.sleep(0.2)
		p.ChangeFrequency(460)
		time.sleep(3.0)
		p.stop()
		time.sleep(1)
		
def STARTUP():
		print ("supi-ka-.." )
		p.start(50)
		p.ChangeFrequency(260)
		time.sleep(0.2)
		p.ChangeFrequency(270)
		time.sleep(0.2)
		p.ChangeFrequency(280)
		time.sleep(0.2)
		p.ChangeFrequency(290)
		time.sleep(0.2)
		p.ChangeFrequency(300)
		time.sleep(0.2)
		p.ChangeFrequency(310)
		time.sleep(0.2)
		p.ChangeFrequency(320)
		time.sleep(0.2)
		p.ChangeFrequency(330)
		time.sleep(0.2)
		p.ChangeFrequency(340)
		time.sleep(0.2)
		p.ChangeFrequency(350)
		time.sleep(0.2)
		p.ChangeFrequency(360)
		time.sleep(0.2)
		p.ChangeFrequency(370)
		time.sleep(0.2)
		p.ChangeFrequency(380)
		time.sleep(0.2)
		p.ChangeFrequency(390)
		time.sleep(0.2)
		p.ChangeFrequency(400)
		time.sleep(0.2)
		p.ChangeFrequency(410)
		time.sleep(0.2)
		p.ChangeFrequency(420)
		time.sleep(0.2)
		p.ChangeFrequency(430)
		time.sleep(0.2)
		p.ChangeFrequency(440)
		time.sleep(0.2)
		p.ChangeFrequency(450)
		time.sleep(0.2)
		p.ChangeFrequency(460)
		time.sleep(0.2)
		p.ChangeFrequency(470)
		time.sleep(0.2)
		p.ChangeFrequency(1)
		time.sleep(0.2)
		p.ChangeFrequency(770)
		time.sleep(0.5)
		p.ChangeFrequency(1)
		time.sleep(0.2)
		p.ChangeFrequency(770)
		time.sleep(0.5)
		p.ChangeFrequency(1)
		time.sleep(0.2)
		p.ChangeFrequency(770)
		time.sleep(2.0)
		p.stop()
		time.sleep(1)
		
#
# このプログラムファイルで動作確認
if  __name__ ==  "__main__":
	try:
		while True:
			OK()
			time.sleep(1)
			NG()
			time.sleep(1)
			CLOCK()
			time.sleep(1)
			END()

	except KeyboardInterrupt:
		END()
		p.stop()
		GPIO.cleanup()

