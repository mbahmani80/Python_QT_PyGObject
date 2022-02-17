#!/usr/bin/env python3
#
# Filename: 03_py_prog_add_two_numbers.py
#
# Copyright (C) 2020 Mahdi Bahmani
#
# 12.05.2020


#-----------------------------------------------------------------------
def AddIt(Value1, Value2):
    print(Value1, " + ", Value2, " = ", (Value1 + Value2))

#-----------------------------------------------------------------------
def main():
	AddIt(2,3)
	Name = input("Tell me your name: ")
	print("Hello ", Name)

#-----------------------------------------------------------------------
if __name__ == "__main__":
  main()
