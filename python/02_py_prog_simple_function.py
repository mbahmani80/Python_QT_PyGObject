#!/usr/bin/env python3
#
# Filename: 02_py_prog_simple_function.py
#
# Copyright (C) 2020 Mahdi Bahmani
#
# 12.05.2020

#-----------------------------------------------------------------------
def simple_function1(Value1):
	print("Calls simple_function1(Value1): ")
	print(Value1)
#-----------------------------------------------------------------------
def simple_function2(Value1, Value2):
	print("Calls simple_function2(Value1, Value2): ")
	print("===================================")
	print(Value1)
	print(Value2)
	print("Value1 type and memory address: ",type(Value1),id(Value1))
	print("Value2 type and memory address: ",type(Value2),id(Value2))
	print("===================================\n")
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
def main():
	simple_function1("Hello world!")
	print("###################################\n")
	simple_function2(10,20)
	
	i = 30
	print (i)
	i = i + 1
	print (i)
		
	s='''This is a multi-line string.
This is the second line.'''
	print (s)
	
	print ("Function 'main' completing.\n")

#-----------------------------------------------------------------------
if __name__ == "__main__":
  main()
