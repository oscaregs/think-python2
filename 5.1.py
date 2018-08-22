"""
Exercise 5.1. 
The time module provides a function, also named time, 
that returns the current Greenwich Mean Time in “the epoch”, 
which is an arbitrary time used as a reference point. 
On UNIX systems, the epoch is 1 January 1970. 

>>> import time 
>>> time.time() 
1437746094.5735958 

Write a script that reads the current time and converts it to a 
time of day in hours, minutes, and seconds, plus the number of days since the epoch.
"""

import time

timeSE = time.time() // 1 #Rounds seconds
minutesSE = timeSE // 60
hoursSE = minutesSE // 60
daysSE = hoursSE // 24

def currentTime(hoursSE, minutesSE, secondsSE):
	print("CURRENT TIME")
	currentHour = hoursSE % 24 
	print("Hour: ", currentHour)
	currentMinute = minutesSE % 60
	print("Minute: ", currentMinute)
	currentSecond = secondsSE % 60
	print("Second", currentSecond)	

currentTime(hoursSE, minutesSE, timeSE)
print("Days since the epoch: ", daysSE)

