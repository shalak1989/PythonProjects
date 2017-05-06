def CelsiusConverter(celsiusTemp):
    return 9/5*int(celsiusTemp) + 32

temperature = input('Enter a temperature to convert to Fahrenheit: ')
print (CelsiusConverter(temperature))
