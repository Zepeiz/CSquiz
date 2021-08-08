
while True:
    celsius = input("\nTemperature in celsius:\n")

    def fahrenheit_from(celsius):
        """Convert Celsius to Fahrenheit degrees."""
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)

    print(fahrenheit_from(celsius))

    answer = input("\nIf you wish to continue, type yes, otherwise type no to exit:\n")
    if answer.lower() == "yes":
        pass
    else:
        break
    pass
