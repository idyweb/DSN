#convert temperature from farenheit to celcius
# first what is the formular for converting farenheit to celcius
# °C = (°F - 32) * 5 / 9

temp = float(input('Enter temperature in fahrenheit: '))

celcius = (temp - 32) * 5/9

print(f'{temp} in Farenheit is equal to {celcius} in Celcius')