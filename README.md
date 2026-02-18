# Fermat's Last Theorem Near Miss Finder

A Python program that searches for near misses to Fermat's Last Theorem for user-specified values of *n* and *k*.

## About

**Fermat's Last Theorem** states that no three positive integers *x*, *y*, and *z* satisfy the equation:

```
x^n + y^n = z^n
```

for any integer value of *n* greater than 2.

This program searches for **near misses** — combinations of integers *x*, *y*, and *z* where *x^n + y^n* is very close to, but not equal to, *z^n*. The program reports each successively smaller relative miss discovered during the search.

## Features

- Interactive command-line interface
- User-defined search parameters (*n* and *k*)
- Calculates both actual miss and relative miss for each near miss found
- Displays results in order of decreasing relative miss
- Pause functionality to review results before continuing

## Requirements

- Python 3.x (if running from source)
- **OR** Windows OS (if using the pre-built executable)

## Installation

### Option 1: Use the Pre-built Executable (Windows Only)

1. Clone this repository or download the `dist/main.exe` file
2. No Python installation required

### Option 2: Run from Source

1. Clone this repository or download the `main.py` file
2. Ensure Python 3.x is installed on your system

## Usage

### Using the Executable (Windows)

Navigate to the `dist` folder and run:

```bash
main.exe
```

Or simply double-click `main.exe` in the file explorer.

### Using Python

Run the program from the command line:

```bash
python main.py
```

### Input Parameters

The program will prompt you for two values:

1. **n** (exponent): An integer where `2 < n < 12`
   - Valid range: 3 to 11 inclusive
   
2. **k** (upper bound): An integer where `k >= 10`
   - Defines the search range for *x* and *y* values: `10 <= x, y <= k`

### Output

The program displays a table with the following columns:

- **x**: First base value
- **y**: Second base value
- **z**: The integer closest to the *n*-th root of *x^n + y^n*
- **Actual Miss**: The absolute difference between *x^n + y^n* and *z^n*
- **Relative Miss**: The actual miss divided by *x^n + y^n*

Each new smallest relative miss is displayed with a pause, allowing you to review the results before continuing (press Enter to proceed).

## Example

```
Welcome to Fermat's Last Theorem Near Miss Finder!

The finder will find print each successive new smallest relative miss for the n and k you provide
such that x^n + y^n is close to z^n for some integers x and y <= k.

Enter an integer for n (where 2 < n < 12): 3

Enter an integer for k such that 10 <= x, y <= k: 50

Successively smaller relative misses for n=3 and k=50:
x       y       z       Actual Miss     Relative Miss

10      10      13      197             0.0985
...
```

## Algorithm Details

The program uses a brute-force search algorithm:

1. Iterates through all combinations of *x* and *y* from 10 to *k*
2. For each combination, finds the value of *z* where *z^n* is closest to *x^n + y^n*
3. Calculates the actual miss: `min(|z^n - (x^n + y^n)|, |(z+1)^n - (x^n + y^n)|)`
4. Calculates the relative miss: `actual miss / (x^n + y^n)`
5. Reports only when a new smallest relative miss is found

## Technical Notes

- The program includes memory error handling to prevent crashes with large values
- For larger values of *k* and *n*, computation time increases significantly
- The search starts at *x*, *y* = 10 to focus on more interesting near misses

## Author Information

- **Programmer**: Alexis Granados
- **Email**: alexisgranados@lewisu.edu
- **Course**: CPSC44000-LT1
- **Date**: February 17, 2025

## License

This is an educational project developed for coursework.
