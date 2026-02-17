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

    userInputs = getUserInputs()
    
    print(f"\nSuccessively smaller relative misses for n={userInputs[0]} and k={userInputs[1]}:")
    print("x\ty\tz\tActual Miss\tRelative Miss\n")

    findFermatNearMisses(userInputs[0], userInputs[1])

def printNearMiss(x, y, z, actualMiss, relativeMiss):
    print(f"{x}\t{y}\t{z}\t{actualMiss:<14}\t{relativeMiss}")

    # Pause after printing each new smallest relative miss to allow the user to see the results before continuing
    input("\nPress Enter to continue...")

def findFermatNearMisses(n, k):
    # Initialize smallestRelativeMiss to infinity to ensure any found miss will be smaller
    smallestRelativeMiss = float('inf')

    for x in range(10, k + 1):
        for y in range(10, k + 1):
            # Start z at the maximum of x and y to ensure we are looking for a near miss where z^n is close to x^n + y^n
            z = max(x, y)
            while True:
                try:
                    if ((z + 1)**n > x**n + y**n) and (z**n < x**n + y**n):
                        break
                except MemoryError:
                    print(f"Memory error for x={x}, y={y}, z={z}. Ending program to prevent further issues.")
                    return
                z += 1
            actualMiss = min(abs((z**n) - (x**n + y**n)), abs((z + 1)**n - (x**n + y**n)))
            relativeMiss = actualMiss / (x**n + y**n)
            if relativeMiss < smallestRelativeMiss:
                smallestRelativeMiss = relativeMiss
                # Check if the next z value (z + 1) provides the smaller miss before printing the current near miss
                if abs((z + 1)**n - (x**n + y**n)) < abs((z)**n - (x**n + y**n)):
                    z += 1
                printNearMiss(x, y, z, actualMiss, relativeMiss)

def getUserInputs():
    userInputs = []

    # Get n from the user, ensuring it's an integer between 3 and 11
    while True:
        userInput = input("Enter an integer for n (where 2 < n < 12): ")
        try:
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
        userInput = input("\nEnter an integer for k such that 10 <= x, y <= k: ")
        try:
            k = int(userInput)
            if k >= 10:
                userInputs.append(k)
                break
            else:
                print("Please enter an integer greater than or equal to 10.")
        except ValueError:
            print("Please enter a valid integer.")
        # Catching large k inputs that may cause performance issues
        except MemoryError:
            print("The value of k is too large and causes memory issues. Please enter a smaller integer.")
    return userInputs

if __name__ == "__main__":
    main()