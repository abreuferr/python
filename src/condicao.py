# autor : caio abreu ferreira
# objetivo : programa utilizado para aprender conficao IF

# inserir os dados
#
# converter do tipo string para tipo int
#
numero1 = int(input("Insira o primeiro valor : "))
numero2 = int(input("Inserir o segundo valor : "))

if numero1 > numero2:
    print("Numeros inseridos ", numero1, numero2) 
    print("O numero ", numero1, "é maior que o numero", numero2)
else:
    print("Numeros inseridos ", numero1, numero2)
    print("O numero ", numero2, "é maior que o numero", numero1)