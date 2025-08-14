# ===================================================================================
# file: hangingout.py
# author: Oracle16
# date: 03/03/2025
# ===================================================================================

# Get fire safety limit and number of events
inputLine = input("")           # get first line of input
parts = inputLine.split()       # split into separate numbers
limit = int(parts[0])          # maximum people allowed
events = int(parts[1])         # number of events to process

currentPeople = 0    # tracks current number of people on terrace
deniedGroups = 0     # tracks number of groups denied entry

# Process each event
for i in range(0, events):
    eventLine = input("")          # get event input
    eventParts = eventLine.split() # split into parts
    action = eventParts[0]         # "enter" or "leave"
    number = int(eventParts[1])    # number of people
    
    # Handle enter attempts
    if action == "enter":
        # Check if adding group would exceed limit
        if currentPeople + number > limit:
            deniedGroups = deniedGroups + 1
        else:
            currentPeople = currentPeople + number
    
    # Handle leave events
    if action == "leave":
        currentPeople = currentPeople - number

# Print final result
print(deniedGroups)
