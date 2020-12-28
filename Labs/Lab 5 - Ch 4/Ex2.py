# Ask the user for a temperature. Then ask them what units,
# Celsius or Fahrenheit, the temperature is in. Your program
# should convert the temperature to the other unit.

temp = float(input("Enter temperature: "))
unit = input("Enter C for celsius and F for fahrenheit: ")
if unit == 'C':
    f = (9./5.) * temp + 32
    print(f"{temp} C = {f} F")
if unit == 'F':
    c = (5./9.) * (temp - 32)
    print(f"{temp} F = {c} C")
