# autor : caio abreu ferreira
# objetivo : programa utilizado para converter de fahrenheit para celsius

# inserir a temperatura em Fahrenheit
tempFahrenheit = input("Digite a temperatura em Fahrenheit : ")

# calcular a temperatura em Celsius
#
# a variavel "tempFahrenheit" eh convertida do tipo string para o tipo float
#
tempCelsius = (float(tempFahrenheit) -32) * 5 / 9

# exibir o resultado da conversao
#
print("a temperatura em Celsius é ", tempCelsius)