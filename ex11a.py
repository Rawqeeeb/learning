print("How much do you weigh in kg?", end=' ')
weight = float(input())
print("How tall are you?", end=' ')
height = float(input())
BMI = weight / height / height
print(f"Your BMI is {BMI}")
