# ===================================================================================
# file: generator.py
# author: Oracle16
# date: 03/27/2025
# ===================================================================================

import random

def preprocess(srcFilename, n):
    """Return the dictionary model for n-gram continuations for given source file."""
    model = {}
    with open(srcFilename, 'r') as file:
        text = file.read()  # Read the entire file as a single string

    # Iterate through the text to build the n-gram model
    for i in range(len(text) - n):
        ngram = text[i:i + n]  # Extract the n-gram
        next_char = text[i + n]  # The character following the n-gram

        # Update the model dictionary
        if ngram not in model:
            model[ngram] = {}
        if next_char not in model[ngram]:
            model[ngram][next_char] = 0
        model[ngram][next_char] += 1

    # Handle the case where the n-gram is at the end of the text
    last_ngram = text[-n:]
    if last_ngram not in model:
        model[last_ngram] = {}
    model[last_ngram][''] = 1  # End of text marker

    return model

def generate(destFilename, model, numChars, initial):
    """Write numChars characters to indicated destination based upon model dictionary."""
    output = initial  # Start the output with the initial n-gram
    current_ngram = initial

    with open(destFilename, 'w') as file:
        file.write(output)  # Write the initial n-gram to the file

        for _ in range(numChars - len(initial)):
            if current_ngram not in model or len(model[current_ngram]) == 0:
                break  # Stop if there are no continuations for the current n-gram

            # Get the possible continuations and their frequencies
            continuations = model[current_ngram]
            total = 0
            for key in continuations:
                total += continuations[key]

            # Choose the next character probabilistically
            rand_val = random.uniform(0, total)
            cumulative = 0
            next_char = ''
            for key in continuations:
                cumulative += continuations[key]
                if rand_val <= cumulative:
                    next_char = key
                    break

            if next_char == '':
                break  # Stop if the end-of-text marker is reached

            output += next_char
            file.write(next_char)  # Write the next character to the file

            # Update the current n-gram
            current_ngram = output[-len(initial):]

    return len(output)

##################################################################
# Main program driver below. Do not edit
##################################################################

if __name__ == '__main__':
    import sys
    import os
    from string import ascii_uppercase
    
    n = 0
    while n <= 0:
        try:
            n = int(input("What value of n for n-grams? "))
            if n <= 0:
                print("Must choose positive n")
        except ValueError:
            print("Invalid integer")
    
    src = None
    while not src:
        filename = input("Input filename? ")
        try:
            fp = open(filename)
            initial = fp.read(n)
            fp.close()
            src = filename
        except IOError:
            print("Unable to read file", filename)
    
    default = filename.split('/')[-1].split('.')[0] + '_' + str(n) + '.txt'
    output = None
    while not output:
        filename = input("Output filename? [default: %s] " % default)
        if not filename:
            filename = default
        try:
            fp = open(filename,'w')
            fp.close()
            output = filename
        except IOError:
            print("Unable to write to file", filename)
    
    total = 0
    while not 0 < total:
        try:
            total = int(input("How many characters of output are desired? "))
            if total <= 0:
                print("Must choose positive value")
        except ValueError:
            print("Invalid integer")
    
    seed = None
    seed = input("Random Seed [press enter if you don't care]: ").strip()
    if not seed:
        seed = ''.join(random.choice(ascii_uppercase) for _ in range(6))
        print('Using seed:', seed)
    random.seed(seed)
    
    model = preprocess(src, n)
    c = generate(output, model, total, initial)
    print(f'Generated {c} characters of output')