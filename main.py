# Program title: Fermat's Last Theorem Near Miss Finder
# Program File: main.py
# External Files: None
# External Files Created: None
# Programmer: Alexis Granados
# Email Address: alexisgranados@lewisu.edu
# Course and Section Numbers: CPSC44000-LT1
# Date of Submission: 02/17/2025
# Description: This program finds near misses to Fermat's Last Theorem for user-inputted values of n and k such that 
# 2 < n < 12 and 10 <= k. It prints  each successive new smallest relative miss for integers x and y less than or equal 
# to k, where x^n + y^n is close to z^n.
# Resource used: https://www.w3schools.com/python/python_reference.asp


def main():

    print("Welcome to Fermat's Last Theorem Near Miss Finder!")
    print("\nThe finder will find print each successive new smallest relative miss for the n and k you provide\n"
          "such that x^n + y^n is close to z^n for some integers x and y <= k.\n")

    # Get user inputs for n and k, ensuring they meet the specified criteria
    userInputs = getUserInputs()
    
    print(f"\nSuccessively smaller relative misses for n={userInputs[0]} and k={userInputs[1]}:")
    print("x\ty\tz\tActual Miss\tRelative Miss\n")

    findFermatNearMisses(userInputs[0], userInputs[1])

# Function to print the details of a near miss, including the actual miss and relative miss, and pause after each new smallest relative miss is found
def printNearMiss(x, y, z, actualMiss, relativeMiss):
    print(f"{x}\t{y}\t{z}\t{actualMiss:<14}\t{relativeMiss}")

    # Pause after printing each new smallest relative miss to allow the user to see the results before continuing
    input("\nPress Enter to continue...")

# Function to find near misses to Fermat's Last Theorem for given n and k, while handling potential memory issues gracefully
def findFermatNearMisses(n, k):

    # Initialize smallestRelativeMiss to infinity to ensure any found miss will be smaller
    smallestRelativeMiss = float('inf')

    # Loop through possible values of x and y starting from 10 up to k
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            # Start z at the maximum of x and y to ensure we are looking for a near miss where z^n is close to x^n + y^n
            z = max(x, y)

            # Increment z until we find the point where z^n exceeds x^n + y^n, while handling potential memory issues that 
            # may arise from large values of n and k
            while True:
                try:
                    if ((z + 1)**n > x**n + y**n) and (z**n < x**n + y**n):
                        break
                except MemoryError:
                    print(f"Memory error for x={x}, y={y}, z={z}. Ending program to prevent further issues.")
                    return
                # If z^n and (z+1)^n does not bound x^n + y^n, increment z to continue searching for the near miss
                z += 1
            
            # Calculate the actual miss for both z and z + 1 to determine which provides the 
            # smaller miss, and then calculate the relative miss
            actualMiss = min(abs((z**n) - (x**n + y**n)), abs((z + 1)**n - (x**n + y**n)))
            relativeMiss = actualMiss / (x**n + y**n)

            
            if relativeMiss < smallestRelativeMiss:
                # Update smallestRelativeMiss to the new smaller relative miss found
                smallestRelativeMiss = relativeMiss

                # Check if the next z value (z + 1) provides the smaller miss
                if abs((z + 1)**n - (x**n + y**n)) < abs((z)**n - (x**n + y**n)):
                    # Update z to z + 1 before printing the near miss details
                    z += 1
                printNearMiss(x, y, z, actualMiss, relativeMiss)

# Function to get user inputs for n and k, ensuring they meet the specified criteria and handling potential memory issues gracefully
def getUserInputs():
    # Initialize an empty list to store user inputs for n and k
    userInputs = []

    # Get n from the user, ensuring it's an integer between 3 and 11
    while True:
        # Prompt the user for n
        userInput = input("Enter an integer for n (where 2 < n < 12): ")
        try:
            # Attempt to convert the user-inputted n to an integer and check if it meets the criteria
            n = int(userInput)
            if 2 < n < 12:
                userInputs.append(n)
                break
            else:
                print("Please enter an integer between 3 and 11.")
        except ValueError:
            print("Please enter a valid integer.")
    
    # Get upper bound k from the user, ensuring k is an integer >= 10
    while True:
        # Prompt the user for k
        userInput = input("\nEnter an integer for k such that 10 <= x, y <= k: ")
        try:
            # Attempt to convert the user-inputted k to an integer and check if it meets the criteria
            k = int(userInput)
            if k >= 10:
                userInputs.append(k)
                break
            else:
                print("Please enter an integer greater than or equal to 10.")
        # Catching non-integer inputs for k and prompting the user to enter a valid integer
        except ValueError:
            print("Please enter a valid integer.")
        # Catching large k inputs that may cause performance issues
        except MemoryError:
            print("The value of k is too large and causes memory issues. Please enter a smaller integer.")
    return userInputs

# The main function is called to start the program when this script is executed
if __name__ == "__main__":
    main()