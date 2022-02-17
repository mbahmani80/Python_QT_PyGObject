#!/usr/bin/env python3
#
# Filename: 09_py_prog_arg.py
#
# Copyright (C) 2020 Mahdi Bahmani
#
# 18.05.2020

import sys

#-----------------------------------------------------------------------
def main():
	try:
		print (sys.argv)
		print (sys.argv[0])
		print (sys.argv[1])
	except IndexError: 
		print ("list index out of range")
#-----------------------------------------------------------------------
if __name__ == "__main__":
  main()
