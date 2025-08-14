# ===================================================================================
# file: symmetric.py
# author: Oracle16
# date: 03/03/2025
# ===================================================================================

setNumber = 1    # tracks which set we're processing

while True:    # keep processing until we get a 0
    # Get number of names in this set
    n = int(input(""))
    
    # Check if we're done lol
    if n == 0:
        break
    
    # Lists to store names for top and bottom parts
    topNames = []        # first half of names
    bottomNames = []     # second half of names
    
    # Read all names and sort them into top/bottom 
    for i in range(0, n):
        name = input("")    # get next name
        
        # We can only use even indices (e.g., 0,2,4...); go to top, odd to bottom
        if i % 2 == 0:
            topNames.append(name)
        else:
            bottomNames.append(name)
    
    # For each input set print “SET” on a line
    print("SET " + str(setNumber))
    
    # Print top names (front to back)
    for name in topNames:
        print(name)
    
    # Print bottom names (back to front)
    for i in range(len(bottomNames)-1, -1, -1):
        print(bottomNames[i])
    
    setNumber = setNumber + 1