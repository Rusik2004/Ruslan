try:
    score = float(input("Enter the score: "))
    if 0 <= score <= 100:
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        print(f"Grade: {grade}")
    else:
        print("Error: Score is out of range (0-100). Please enter a valid score.")
except ValueError:
    print("Error, please enter numeric input between 0 and 100")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
