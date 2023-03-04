import math

def is_prime(n):
    """Return True if n is a prime number, False otherwise."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

while True:
    # Ask the user to enter a number
    n = input("Enter a number (or 'q' to quit): ")
    
    # Check if the user wants to quit
    if n.lower() == 'q':
        print("Exiting program.")
        break
    
    # Convert the input to an integer
    try:
        n = int(n)
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")
        continue
    
    # Check if the number is prime
    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
