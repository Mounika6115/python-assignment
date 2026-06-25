# Initialize the starting number
num = 1
# Loop while num is less than or equal to 10
while num <= 10:
    # Stop the loop when num becomes 8
    if num == 8:
        print("Encountered 8. Stopping the loop.")
        break  # Exits the loop completely
    # Skip odd numbers
    if num % 2 != 0:
        num += 1
        continue  # Skips the rest of the current iteration
    # Print even numbers
    print(num)
    # Move to the next number
    num += 1