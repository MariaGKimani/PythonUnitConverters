def pounds_to_kilograms(pounds):
    kilograms = pounds / 2.205
    return kilograms

pounds = float(input("Enter weight in pounds: "))
kilograms  = pounds_to_kilograms(pounds)
print(f"The weight in kilograms is: {kilograms} kg")