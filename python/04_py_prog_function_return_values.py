#!/usr/bin/env python3
#
# Filename: 04_py_prog_function_return_values.py
#
# Copyright (C) 2020 Mahdi Bahmani
#
# 12.05.2020


#-----------------------------------------------------------------------

def AddIt(Value1, Value2):
    print(Value1, " + ", Value2, " = ", (Value1 + Value2))
########################################################################
    
#-----------------------------------------------------------------------

def calc_value (bas, quux):
	# This function returns a value.
	return bas * quux;
########################################################################

#-----------------------------------------------------------------------

def main():
	AddIt(2,3)
	AddIt(calc_value(10,20),3)

#-----------------------------------------------------------------------
if __name__ == "__main__":
  main()
