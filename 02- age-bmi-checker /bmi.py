# --- AGE CHECKER ---
print("--- AGE CHECKER ---")
birth_year = int(input("Enter your birth year (e.g. 2002): "))
current_year = 2026
age = current_year - birth_year

print("You are", age, "years old.")

if age < 13:
    print("You are a Child")
elif age < 20:
    print("You are a Teenager")
elif age < 60:
    print("You are an Adult")
else:
    print("You are a Senior Citizen")

# --- BMI CHECKER ---
print("\n--- BMI CHECKER ---")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters (e.g. 1.75): "))

bmi = weight / (height * height)
print("\nYour BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight - Eat more healthy food")
elif bmi < 25:
    print("Category: Normal - Good job! Keep it up")
elif bmi < 30:
    print("Category: Overweight - Do some exercise")
else:
    print("Category: Obese - Please consult doctor and exercise")
