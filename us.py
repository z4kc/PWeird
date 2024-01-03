#!/usr/bin/env python2
import os
import random
import time
import pyfiglet as pfg
from termcolor import colored
from pyfiglet import figlet_format
while True:

	def c():
		os.system("clear")
	def mil5():
		time.sleep(0.2)
	def red(msg):
		print(f"\033[5;49;91m {msg}\033[m")
	def gren(msg):
		print(f"\033[5;49;92m {msg}\033[m")
	def ylw(msg):
		print(f"\033[5;49;93m {msg}\033[m")
	def dblue(msg):
		print(f"\033[5;49;94m {msg}\033[m")
	def rose(msg):
		print(f"\033[5;49;95m {msg}\033[m")
	def blue(msg):
		print(f"\033[5;49;96m {msg}\033[m")
	def wt(msg):
		print(f"\033[5;49;97m {msg}\033[m")
	respfire = random.randint(100,999)
	res = random.randint(100,999)
	rank = random.randint(100,999)
	ram = random.randint(100,999)
	respk = random.randint(100,999)
	ranso = random.randint(100,999)
	c()
	mil5()
	print((colored(figlet_format("WPPVC"), color="light_green")))
	mil5()
	red("\/"*20)
	red("")
	mil5()
	gren("[ 1 ] Basic VC")
	red("")
	mil5()
	gren("[ 2 ] Medium VC")
	red("")
	mil5()
	gren("[ 3 ] Advanced VC")
	red("")
	mil5()
	gren("[ 0 ] Menu")
	red("")
	mil5()
	red("\/"*20)
	print("")
	resp = int(input("localhost@u_2777a: "))
	if(resp == 1):
		print(f"{respfire}-{res}")
		input()
		continue
	if(resp == 2):
		print(f"{respfire}-{res}")
		print(f"{ram}-{rank}")
		input()
		continue
	if(resp == 3):
		print(f"{respfire}-{res}")
		print(f"{ram}-{rank}")
		print(f"{respk}-{ranso}")
		input()
		continue
	if(resp == 0):
		os.system("python password.py")
		break
	else:
		print("[ ! ] PROPIEDADE INDEFINIDA")
		continue

