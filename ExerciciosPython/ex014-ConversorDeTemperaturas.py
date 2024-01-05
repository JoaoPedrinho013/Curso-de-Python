#Crie um programa que converta uma temperatura em Celsius para outras temperaturas
c = float(input('Digite uma temperatura em °C:'))
f = 9 * c / 5 + 32
k = c + 273.15
print(f'A temperatura de {c:.1f}°C \nEm Fahrenheit é {f:.1f}°F \nEm Kelvin é {k:.2f}K ')
