# Write a program that asks the user to enter a length. The program
# should ask them what unit the length is in and what unit they would
# like to convert it to. The possible units are inches, yards, miles,
# millimeters, centimeters, meters, and kilometers. While this can be
# done with 25 if statements, it is shorter and easier to add on to if
# you use a two-dimensional list of conversions, so please use lists
# for this problem.

mults = [
    [1, 0.0277777778, 0.0000157828, 25.4, 2.54, 0.0254, 0.0000254],
    [36, 1, 0.0005681797, 914.4, 91.44, 0.9144, 0.0009144],
    [63360, 1760, 1, 1609344, 160934.4, 1609.344, 1.609344],
    [0.0393700787, 0.0010936133, 6.213688756e-7, 1, 0.1, 0.001, 0.000001],
    [0.3937007874, 0.010936133, 0.0000062137, 10, 1, 0.01, 0.00001],
    [39.37007874, 1.0936132983, 0.0006213689, 1000, 100, 1, 0.001],
    [39370.07874, 1093.6132983, 0.6213688756, 1000000, 100000, 1000, 1]
]
inp = eval(input("Please enter a length: "))
inUnit = int(
    input("Select input Unit: \n1: in\n2: yd\n3: miles\n4: mm\n5: cm\n6: m\n7: km\n")) - 1
outUnit = int(
    input("Select output Unit: \n1: in\n2: yd\n3: miles\n4: mm\n5: cm\n6: m\n7: km\n")) - 1
print("Converted Length:", inp * mults[inUnit][outUnit])
