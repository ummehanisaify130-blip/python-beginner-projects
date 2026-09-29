print("--- UNIT CONVERTER ---")
print("1. Length (km to miles)")
print("2. Weight (kg to pounds)")
print("3. Temperature (Celsius to Fahrenheit)")

choice = input("Choose (1-3): ")

if choice == '1':
    km = float(input("Enter km: "))
    miles = km * 0.621371
    print(km,"km","=",miles,"miles")

elif choice == '2':
    kg = float(input("Enter kg: "))
    pounds = kg * 2.20462
    print(kg,"kg","=",pounds,"pounds")

elif choice == '3':
    c = float(input("Enter Celsius: "))
    f = (c * 9/5) + 32
    print(c,"°C","=",f,"°F")

else:
    print("Invalid choice!")
