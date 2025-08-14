# ===================================================================================
# file: dna.py (using split method of the string class)
# author: Oracle16
# date: 02/08/2025
# ===================================================================================

# Get user input
dnaSequence = input("Enter a DNA sequence: ").upper()
pattern = input("Enter the pattern: ").upper()

# Reverse the pattern
reversedPattern = pattern[::-1]

# Split the DNA sequence at the first occurrence of the pattern
parts = dnaSequence.split(pattern, 1)
if len(parts) < 2:
   print("Pattern not found in DNA sequence.")
else:
   prefix = parts[0]
   rest = parts[1]

   # Split the remaining part at the first occurrence of the reversed pattern
   parts = rest.split(reversedPattern, 1)
   if len(parts) < 2:
       print("Reversed pattern not found in DNA sequence.")
   else:
       middle = parts[0]
       suffix = parts[1]

       # Reverse the middle part
       reversedMiddle = middle[::-1]

       # Construct the mutated DNA sequence
       mutatedDna = prefix + pattern + reversedMiddle + reversedPattern + suffix

       # Output in the required format
       if prefix:
           print("Prefix: " + prefix)
       else:
           print("Prefix: ")

       print("Marker: " + pattern)

       if middle:
           print("Middle: " + middle)
       else:
           print("Middle: ")

       if reversedMiddle:
           print("Reversed Middle: " + reversedMiddle)
       else:
           print("Reversed Middle: ")

       print("Reversed Marker: " + reversedPattern)

       if suffix:
           print("Suffix: " + suffix)
       else:
           print("Suffix: ")

       print("Result: " + mutatedDna)