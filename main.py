# 1. Define a function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

# 2. Print a simple message to the console
print("--- Welcome to the Python Sample Program ---")

# 3. Take user input and handle data types
try:
    user_name = input("Enter your name: ")
    user_num = int(input("Enter a whole number to check: "))
    
    # Greet the user
    print(f"\nHello, {user_name}!")
    
    # Call the function and print the result
    result = check_even_odd(user_num)
    print(result)

except ValueError:
    print("Error: Please make sure to enter a valid integer next time.")

# 4. Use a simple loop to count from 1 to 3
print("\nCounting down your next steps:")
for i in range(1, 4):
    print(f"Step {i}...")

print("Happy Coding!")
