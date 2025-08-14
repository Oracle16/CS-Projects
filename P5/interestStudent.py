##################################################################
# Student contributions to the interest calculator
#
# You are free to add additional utility functions as you see fit,
# but you must implement each of the following functions while
# adhering to the specifications given in the project description
##################################################################

#---------------------------------------------------------------------------------
# function to only display initial text
def greeting():
    print("This interest calculator will ask you to select an interest rate,")
    print("followed by a principal value. It will then calculate and display")
    print("the principal, interest rate, and balance after one year. You will")
    print("then be invited to execute the process again or terminate.")

#---------------------------------------------------------------------------------
# use while loop to repeatedly prompt user until valid input
def getRate(choices):
    while True:
        print("\nPlease select an interest rate:")
        for i, choice in enumerate(choices):
            # Label % Choices: ASCII (and Unicode) code point for the uppercase letter "A" is 65
            print(f"{chr(65 + i)}) {choice}%")
        selection = input("Enter A-{}: ".format(chr(65 + len(choices) - 1))).strip().upper()
        # shorthand
        if selection in [chr(65 + i) for i in range(len(choices))]:
            return choices[ord(selection) - 65] / 100.0  # Convert percentage to decimal
        else:
            print("That is not a valid selection.")

#---------------------------------------------------------------------------------
# use while loop until valid input is recieved
def getPrincipal(limit):
    while True:
        principal = input(f"\nEnter the principal (limit {limit}): ").strip()
        if principal.startswith("$"):
            principal = principal[1:]  # Remove dollar sign if present

        try:
            principal = float(principal)
            if principal <= 0:
                print("You must enter a positive amount.")
            elif principal > limit:
                print(f"The principal can be at most {limit}.")
            elif round(principal, 2) != principal:
                print("The principal must be specified in dollars and cents.")
            else:
                return principal
        except ValueError:
            print("Please enter a number.")

#---------------------------------------------------------------------------------
def computeBalance(principal, rate):
    return principal + (principal * rate)

#---------------------------------------------------------------------------------
def displayTable(principal, rate, balance):
    # proper formatting of displayed results
    print("\nInitial Principal   Interest Rate   End of Year Balance")
    print("=======================================================")
    print(f"${principal:,.2f}             {rate:.2f}            ${balance:,.2f}")

#---------------------------------------------------------------------------------
# extra credit function: display interest when compounded over twelve months of the year
def displayTableExtra(principal, rate, balance):
    # provided formula
    monthly_rate = pow(1 + rate, 1.0 / 12) - 1
    print("\nMonth   Starting Balance    APR     Ending Balance")
    print("==================================================")
    for month in range(1, 13):
        ending_balance = principal + (principal * monthly_rate)
        print(f"{month:>3}     ${principal:,.2f}            {rate:.2f}    ${ending_balance:,.2f}")
        principal = ending_balance

#---------------------------------------------------------------------------------
def askYesNo(prompt):
    while True:
        # clean up input
        response = input(prompt).strip().lower()
        # accept any line that has either 'y' or 'Y' as the first non-blank character to indicate yes
        if response.startswith("y"):
            return True
        # accept any line that has either 'n' or 'N' as the first non-black character to indicate no
        elif response.startswith("n"):
            return False
        # if all else fails, try again!
        else:
            print("Please enter 'y' or 'n'.\n")

#---------------------------------------------------------------------------------
if __name__ == "__main__":
    greeting()
    while True:
        # Step 1: Get the interest rate (can change 10 to 12 for extra credit example)
        rate = getRate([3, 5, 7, 10])

        # Step 2: Get the principal amount
        principal = getPrincipal(700000)

        # Step 3: Compute the year-end balance
        balance = computeBalance(principal, rate)

        # Step 4: Display the results in a table
        displayTable(principal, rate, balance)

        '''
        # Step 5 (optional): Display the extra credit table (compounded monthly)
        print("\nWould you like to see the monthly compounded interest table?")
        if askYesNo("[y/n]? "):
            displayTableExtra(principal, rate, balance)
        '''

        # Step 6: Ask if the user wants to perform another computation
        if askYesNo("\nAnother Computation [y/n]? "):
            continue
        else:
            print("Quitting program. Bye.")
            break