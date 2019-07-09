import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

PIN_led1 = 11
PIN_led2 = 5
PIN_led3 = 6
PIN_led4 = 13
PIN_led5 = 19
PIN_led6 = 26

OFF = 0
ON = 1
TENNMETU_ZIKANN =0.5
TENNMETU_ZIKANN2=0.2

GPIO.setup(PIN_led1, GPIO.OUT)
GPIO.setup(PIN_led2, GPIO.OUT)
GPIO.setup(PIN_led3, GPIO.OUT)
GPIO.setup(PIN_led4, GPIO.OUT)
GPIO.setup(PIN_led5, GPIO.OUT)
GPIO.setup(PIN_led6, GPIO.OUT)

#-------------------------------------------
def red(mode):
		print("red")
		if mode == ON:
		# on
			GPIO.output(PIN_led1, ON)
			GPIO.output(PIN_led3, ON)
			GPIO.output(PIN_led5, ON)
			
		elif mode== OFF:
		# off
			GPIO.output(PIN_led1,OFF)
			GPIO.output(PIN_led3,OFF)
			GPIO.output(PIN_led5,OFF)

def blue(mode):
		print("blue")
		if mode == ON:
			# on
			red(OFF)
			GPIO.output(PIN_led2, ON)
			GPIO.output(PIN_led4, ON)
			GPIO.output(PIN_led6, ON)
			
		elif mode== OFF:
			# off
			red(OFF)
			GPIO.output(PIN_led2,OFF)
			GPIO.output(PIN_led4,OFF)
			GPIO.output(PIN_led6,OFF)
			
def all(mode):
		print("all")
		if mode == ON:
			# on
			red(ON)
			blue(ON)			
			
		elif mode== OFF:
			# off
			red(OFF)
			blue(OFF)				
			
def red_blink(times):
		print("red blink")
		i=0
		while i < times :
			# on
			red(ON)			
			time.sleep(TENNMETU_ZIKANN)
			# off
			red(OFF)	
			time.sleep(TENNMETU_ZIKANN)
			i += 1			

def blue_blink(times):
		print("blue blink")
		i=0
		while i < times :
			# on
			blue(ON)			
			time.sleep(TENNMETU_ZIKANN)
			# off
			blue(OFF)	
			time.sleep(TENNMETU_ZIKANN)
			i += 1			
			
def all_blink(times): 
		print("all blink")
		i=0
		while i < times :
			# on
			blue(ON)
			red(ON)			
			time.sleep(TENNMETU_ZIKANN)
			# off
			blue(OFF)
			red(OFF)	
			time.sleep(TENNMETU_ZIKANN)
			i += 1			

def led_ONOFF(number,mode ):
		if number ==1 and mode == ON:
			GPIO.output(PIN_led1, ON)
		if number ==1 and mode == OFF:
			GPIO.output(PIN_led1, OFF)
		#------	
		if number ==2 and mode == ON:
			GPIO.output(PIN_led2, ON)
		if number ==2 and mode == OFF:
			GPIO.output(PIN_led2, OFF)
	#------	
		if number ==3 and mode == ON:
			GPIO.output(PIN_led3, ON)
		if number ==3 and mode == OFF:
			GPIO.output(PIN_led3, OFF)
#------	
		if number ==4 and mode == ON:
			GPIO.output(PIN_led4, ON)
		if number ==4 and mode == OFF:
			GPIO.output(PIN_led4, OFF)
#------	
		if number ==5 and mode == ON:
			GPIO.output(PIN_led5, ON)
		if number ==5 and mode == OFF:
			GPIO.output(PIN_led5, OFF)
#------	
		if number ==6 and mode == ON:
			GPIO.output(PIN_led6, ON)
		if number ==6 and mode == OFF:
			GPIO.output(PIN_led6, OFF)			
	#------	
				
def seq_forward(times):
		print("seq forward")
		all(OFF)
		j=0
		while j < times :
			i=1
			while  i< 8 :
				led_ONOFF(i, ON)
				led_ONOFF(i-1, OFF)				
				time.sleep(TENNMETU_ZIKANN2)
				i+=1	
			j+=1
			
def seq_back(times):
		print("seq forward")
		all(OFF)
		j=0
		while j < times :
			i=8
			while  i> -1 :
				led_ONOFF(i, ON)
				led_ONOFF(i+1, OFF)				
				time.sleep(TENNMETU_ZIKANN2)
				i-=1	
			j+=1
#-------------------------------------------


def STARTUP():
		print ("led.START." )
		GPIO.output(PIN_led1,0)
		GPIO.output(PIN_led2,0)
		GPIO.output(PIN_led3,0)
		GPIO.output(PIN_led4,0)
		GPIO.output(PIN_led5,0)
		GPIO.output(PIN_led6,0)
		time.sleep(1)
		GPIO.output(PIN_led1,1)               
		GPIO.output(PIN_led2,1)
		GPIO.output(PIN_led3,1)
		GPIO.output(PIN_led4,1)
		GPIO.output(PIN_led5,1)
		GPIO.output(PIN_led6,1)
		time.sleep(1)

def OK():
		print ("led.OK." )
		GPIO.output(PIN_led2,0)
		GPIO.output(PIN_led4,0)
		GPIO.output(PIN_led6,0)
		time.sleep(0.5)
		GPIO.output(PIN_led2,1)
		GPIO.output(PIN_led4,1)
		GPIO.output(PIN_led6,1)          
		time.sleep(1)
		
		
def NG():
		print ("led.NG.")
	
		time.sleep(1)


def CLOCK():
		print ("led.CROCK.")

		time.sleep(1)

	
def END():
		print ("led.END.")

		time.sleep(1)



# このプログラムファイルで動作確認
if  __name__ ==  "__main__":
	try:
		while True:
			seq_back(5)
			continue
			
			red(ON)
			time.sleep(1)
			red(OFF)
			time.sleep(1)
			#----------------
			blue(ON)
			time.sleep(1)
			blue(OFF)
			time.sleep(1)
			#--------------
			all(ON)
			time.sleep(1)
			all(OFF)
			time.sleep(1)
			#--------
			red_blink(3)#-------------------------------------------
			time.sleep(1)
			blue_blink(3)
			time.sleep(1)
			all_blink(3)			
			
	except KeyboardInterrupt:
		GPIO.cleanup()


