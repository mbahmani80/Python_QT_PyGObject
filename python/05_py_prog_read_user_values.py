#!/usr/bin/env python3
#
# Filename: 05_py_prog_read_user_values.py
#
# Copyright (C) 2020 Mahdi Bahmani
#
# 12.05.2020


#-----------------------------------------------------------------------

def AddIt(Value1, Value2):
	int1 = input("Enter first integer: ")
	int2 = input("Enter second integer: ")
	sum1 = int(int1) + int(int2)
	print("Sum: ", int1, "+", int2, "=",sum1)
	
	
########################################################################

#-----------------------------------------------------------------------

def main():
	AddIt(2,3)

#-----------------------------------------------------------------------
if __name__ == "__main__":
  main()
