# Asking user for the input 

user_input = float(input("Enter temperature in Celcius: "))

# Conversions 
farneheit = (user_input * 1.8) + 32
kelvin = user_input + 273.15

# Printing the results 
print(f'Temperature in Farenheit: {farneheit}')
print(f'Temperature in Kelvin: {kelvin}')