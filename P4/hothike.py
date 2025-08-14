# ===================================================================================
# file: hothike.py
# author: Oracle16
# date: 03/03/2025
# ===================================================================================

# Get the number of days
n = int(input(""))    # length of vacation in days

# Get temperatures as a string and convert to list "temps"
tempString = input("")      # get full line of temperatures
tempParts = tempString.split()    # split into separate numbers
temps = []                        # list to store temperatures

# Convert each temperature from string to integer
for i in range(0, n):
    temps.append(int(tempParts[i]))

bestDay = 1          # we need to set the best starting day at 1 instead of 0
minMaxTemp = 9999    # minimum of maximum temperatures

# Check each possible 3-day period
for i in range(n - 2):
    day1Temp = temps[i]        # first hiking day
    day3Temp = temps[i + 2]    # second hiking day (after rest day)! skips middle
    
    # Get maximum temperature between hiking days
    if day1Temp > day3Temp:
        maxTemp = day1Temp
    else:
        maxTemp = day3Temp
    
    # Update if we found better maximum temperature
    if maxTemp < minMaxTemp:
        minMaxTemp = maxTemp
        bestDay = i + 1    # adding 1 for each additional day

print(bestDay, minMaxTemp)