class Temperature:
    def celsius_fahrenheit(self, c):
        if 0 <= c <= 100:
            f = ((9 / 5) * c) + 32
            return f
        else:
            raise ValueError("Temperature must be between 0 and 100 Celsius.")

    def fahrenheit_celsius(self, f):
        if 32 <= f <= 212:
            c = (f - 32) * (5 / 9)
            return c
        else:
            raise ValueError("Temperature must be between 32 and 212 Fahrenheit.")


def get_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


t = Temperature()
x = get_input("Enter the temperature: ")
unit = input("Enter its units (celsius or fahrenheit): ")

if unit == 'celsius':
    try:
        print(f'The temperature {x} {unit} when converted to fahrenheit: {t.celsius_fahrenheit(x)}')
    except ValueError as e:
        print(e)
elif unit == 'fahrenheit':
    try:
        print(f'The temperature {x} {unit} when converted to celsius: {t.fahrenheit_celsius(x)}')
    except ValueError as e:
        print(e)
else:
    print("The unit is invalid. Please enter a valid unit (celsius or fahrenheit).")
