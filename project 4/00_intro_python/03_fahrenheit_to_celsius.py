def main():
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

    print("Temperature:", str(degrees_fahrenheit) + "F =", str(degrees_celsius) + "C")

main()