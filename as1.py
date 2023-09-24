try:
    hours = input("Enter hours worked: ")
    rate = input("Enter hourly rate: ")
    try:
        hours = float(hours)
        rate = float(rate)
    except ValueError:
        raise ValueError("Hours and rate must be numeric values.")
    if hours > 40:
        regular_salary = 40 * rate
        overtime_hours = hours - 40
        overtime_salary = overtime_hours * (1.5 * rate)
        total_salary = regular_salary + overtime_salary
    else:
        total_salary = hours * rate
    print(f"Total salary: ${total_salary:.2f}")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
