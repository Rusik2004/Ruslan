total = 0
count = 0

while True:
    try:
        user_input = input("Enter a number or 'done' to finish: ")
        if user_input.lower() == 'done':
            break
        number = float(user_input)
        total += number
        count += 1
    except ValueError:
        print("Error: Please enter a valid number or 'done'.")
if count > 0:
    average = total / count
    print(f"Sum: {total}")
    print(f"Count: {count}")
    print(f"Average: {average:.2f}")
else:
    print("No valid numbers entered.")
