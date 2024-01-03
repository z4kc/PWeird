#!/usr/bin/env python2
import string
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
	c()
	mil5()
	print((colored(figlet_format("WRR"), color="light_green")))
	mil5()
	red("\/"*20)
	red("")
	mil5()
	gren("[ 1 ] Try Break Router Password")
	red("")
	mil5()
	gren("[ 0 ] Menu")
	red("")
	mil5()
	red("\/"*20)
	print("")
	resp = int(input("localhost@u_2777a: "))
	if(resp == 1):
		renk = input("Type the Router WiFi Name: ")
		rsp = renk.lower()
		rep = renk.upper()
		red("The Most Probably Bases: ")
		mil5()
		gren(rsp)
		gren(rep)
		r1 = input("Type it the actual year or an very important year: ")
		r2 = input("Continue: ")
		r3 = input("Continue: ")
		r4 = input("Continue: ")
		red("")
		mil5()
		gren("Bulding Possibles PassWords...")
		mil5()
		rose(f"{rsp}{r1}{r2}{r3}{r4}")
		rose(f"{rsp}{r4}{r3}{r2}{r1}")
		rose(f"{rsp}{r1}{r3}{r2}{r4}")
		rose(f"{rep}{r1}{r2}{r3}{r4}")
		rose(f"{rep}{r4}{r3}{r2}{r1}")
		rose(f"{rep}1{r3}{r2}{r4}")
		rose(f"{rsp}2{r2}{r3}{r4}")
		rose(f"{rsp}3{r3}{r2}{r1}")
		rose(f"{rsp}4{r3}{r2}{r4}")
		rose(f"{rep}5{r2}{r3}{r4}")
		rose(f"{rep}6{r3}{r2}{r1}")
		rose(f"{rep}1{r3}{r2}2")
		ylw(f"{rsp}{r1}{r3}{r4}{r2}")
		ylw(f"{rsp}{r2}{r3}{r1}{r4}")
		ylw(f"{rsp}{r1}{r2}{r3}{r4}")
		ylw(f"{rsp}{r4}{r1}{r3}{r2}")
		ylw(f"{rep}{r1}{r3}{r4}{r2}")
		ylw(f"{rep}{r2}{r3}{r1}{r4}")
		ylw(f"{rep}{r1}{r2}{r3}{r4}")
		ylw(f"{rep}{r4}{r1}{r3}{r2}")
		blue(f"{rsp}{r1}{r3}{r4}1")
		blue(f"{rsp}{r2}{r3}{r1}2")
		blue(f"{rsp}{r1}{r2}{r3}3")
		blue(f"{rsp}{r4}{r1}{r3}4")
		blue(f"{rsp}{r1}{r3}{r4}5")
		blue(f"{rsp}{r2}{r3}{r1}6")
		blue(f"{rsp}{r1}{r2}{r3}7")
		blue(f"{rsp}{r4}{r1}{r3}8")
		blue(f"{rsp}{r4}{r1}{r3}9")
		blue(f"{rep}{r1}{r3}{r4}1")
		blue(f"{rep}{r2}{r3}{r1}2")
		blue(f"{rep}{r1}{r2}{r3}3")
		blue(f"{rep}{r4}{r1}{r3}4")
		blue(f"{rep}{r1}{r3}{r4}5")
		blue(f"{rep}{r2}{r3}{r1}6")
		blue(f"{rep}{r1}{r2}{r3}7")
		blue(f"{rep}{r4}{r1}{r3}8")
		blue(f"{rep}{r4}{r1}{r3}9")
		
		input()
		continue
	if(resp == 0):
		os.system("python password.py")
		break
	else:
		print("[ ! ] PROPIEDADE INDEFINIDA")
		continue

