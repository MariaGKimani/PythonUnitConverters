def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin


celsius = float(input("Enter temperature in Celsius: "))
kelvin = celsius_to_kelvin(celsius)
print(f"The temperature in Kelvin is: {kelvin} K")
