#!/usr/bin/env python3
#
# Filename: 13_py_DataType_number.py
#
# Copyright (C) 2020 Mahdi Bahmani
#
# 18.05.2020

import sys

#-----------------------------------------------------------------------
def main():
	print ("======================================")
	num1=12
	num2=4
	num3=4
	print(num1/num2)
	print(num1%num2)
	
	print ("======================================")
	flot1=12.4
	flot2=3.2
	print(flot1/flot2)
	print(flot1%flot2)
	
	print ("======================================")
	print(num1<num2)
	print(num1>num2)
	print(num3>=num2)
	print(num3==num2)
	print(num3!=num2)
	
	print ("======================================")
	print(3/2)
	print(3/2.0)
	print(100 - 5**2 / 5 * 2)
	
	print ("======================================")
	print(int(1.5))
	print(float(2))
	
	print ("======================================")
	print(abs(6))
	print(abs(-6))
	
	print ("======================================")
	print(max(10,20))
	print(min(10,20))
	print(pow(5,2))
	print(5**2)
	
	
#-----------------------------------------------------------------------
if __name__ == "__main__":
  main()
