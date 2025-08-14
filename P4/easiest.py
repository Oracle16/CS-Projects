# ===================================================================================
# file: easiest.py
# author: Oracle16
# date: 03/03/2025
# ===================================================================================

# Make sum digits in a number process less repetitive
def sumDigits(num):
    total = 0
    numStr = str(num)    # convert to string to process digits
    
    # Add up each digit
    for digit in numStr:
        total = total + int(digit)
    
    return total

# Process numbers until we get a 0
while True:
    # Get the number N
    N = int(input(""))
    
    # Check if we're done
    if N == 0:
        break
    
    nSum = sumDigits(N)    # sum of digits in N
    p = 11                 # start checking from 11 (must be > 10)
    
    # Keep trying values of p until we find one that works
    while True:
        product = N * p    # multiply N by p
        productSum = sumDigits(product)    # sum digits in product
        
        # Check if we found a match
        if productSum == nSum:
            print(p)    # found our answer
            break
        
        p = p + 1    # try next number