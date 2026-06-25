while True:
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Error: Please enter a positive integer greater than 0.")
        else:
            break
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
total = 0
counter = 1
while counter <= num:
    total += counter
    counter += 1
print(f"The sum of numbers from 1 to {num} is: {total}")