# mileage converter

print("How many kilometers did you run today?")
kilometers = input()
miles = float(kilometers) / 1.60934
miles = round(miles, 3)
print(f"You ran {miles} miles today!")


