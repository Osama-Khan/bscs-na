# Ask the user to enter a temperature in Celsius. The program
# should print a message based on the temperature.
temp = float(input("Enter temperature: "))
msg = "above the boiling point"
if temp < -273.15:
    msg = "invalid"
elif temp == -273.15:
    msg = "absolute 0"
elif temp < 0:
    msg = "below freezing"
elif temp == 0:
    msg = "at the freezing point"
elif temp < 100:
    msg = "in the normal range"
elif temp == 100:
    msg = "at the boiling point"

print(f"The temperature is {msg}")
