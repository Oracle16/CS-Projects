# ===================================================================================
# file: dnaExtra.py (using index method of a string)
# author: Oracle16
# date: 02/08/2025
# ===================================================================================

# Get user input
dnaSequence = input("Enter a DNA sequence: ").upper()
pattern = input("Enter the pattern: ").upper()

# Reverse the pattern
reversedPattern = pattern[::-1]

# Find the first occurrence of the pattern
try:
    firstIndex = dnaSequence.index(pattern)
except ValueError:
    print("Pattern not found in DNA sequence.")
    exit()

# Find the first occurrence of the reversed pattern after the pattern
try:
    secondIndex = dnaSequence.index(reversedPattern, firstIndex + len(pattern))
except ValueError:
    print("Reversed pattern not found in DNA sequence.")
    exit()

# Extract different parts of the sequence
prefix = dnaSequence[:firstIndex]
middle = dnaSequence[firstIndex + len(pattern):secondIndex]
suffix = dnaSequence[secondIndex + len(reversedPattern):]

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