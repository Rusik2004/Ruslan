# Get input from the user in seconds
total_seconds = int(input("Enter seconds: "))

# Calculate hours, minutes, and remaining seconds
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# Print the result
print(f"{total_seconds} seconds is {hours} hours, {minutes} minutes, {seconds} seconds")