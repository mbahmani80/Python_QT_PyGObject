#!/usr/bin/env python3
#
# Filename: 19_py_Countdown_Clock.py
#
# Copyright (C) 2020 Mahdi Bahmani
#
# 07.06.2020

import time
#-----------------------------------------------------------------------
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        #print(timeformat)
        time.sleep(1)
        t -= 1
    print('Goodbye!\n\n\n\n\n')

#-----------------------------------------------------------------------
def main():
	
	t = input("Enter Time (seconds) : ")
	print('This window will remain open for {t1} more seconds...'.format(t1=t))
	countdown(int(t))
	
	
#-----------------------------------------------------------------------
if __name__ == "__main__":
  main()
