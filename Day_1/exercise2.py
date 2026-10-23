marks = float(input("Enter your marks between 0 and 100: "))

if marks >= 80:
    print("Excellent")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Pass")
elif marks < 0 and marks > 100:
    print("Invalid marks!")