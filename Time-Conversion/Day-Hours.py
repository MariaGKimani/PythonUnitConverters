def days_to_hours(days):
    hours = days * 24
    return hours


days = float(input("Enter the number of days: "))
hours = days_to_hours(days)
print(f"{days} days is equivalent  to {hours} hours")
