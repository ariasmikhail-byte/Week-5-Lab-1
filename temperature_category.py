# Mikhail Arias 
# CMP - 131
# Week 5
# Lab 1
print("===============================")
print("     Temperature Catagorizer:")
print("===============================")
# User Input
temp = float(input("Enter the temperature in degrees Fahrenheit:"))

# Check temperature category
if temp < 50:
    category = "Cold"
elif temp < 80:
    category = "Warm"
else:
    category = "Hot"


# Display result
print("Temperature:", temp, "°F")
print("Category:", category)



    