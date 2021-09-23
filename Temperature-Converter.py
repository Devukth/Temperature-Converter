print("Temperature Converter - Celsius to Fahrenheit")
print("---------------------------------------")

temp = float(input("What is the temperature? (Celsius): "))
converted = (temp * 1.8) + 32

print("%0.1f°C is equal to %0.1f°F" %(temp, converted))

if (converted >= 104):
    print("It's hot.")

elif (converted <= 50):
    print("It's cold.")

else:
    print("It's nice weather.")