# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRICAO  : converter segundos em dias, horas, minutos e segundos
# OBS: // = parte inteira, % = resto

# inserir os dados
segundos_string = input("Por favor, entre com o número de segundos que deseja converter: ")
segundos_inteiro = int(segundos_string)

# calcular o numero de dias
total_dia = (((segundos_inteiro)//60)//60)//24

# calcular o numero de horas
total_hora = (((segundos_inteiro)//60)//60)%24

# calcular o numero de minutos
total_minuto = (segundos_inteiro//60)%60

# calcular o numero de segundos
total_segundos = (segundos_inteiro)%60

# exibir o resultado
print(total_dia, "dias,", total_hora,"horas,", total_minuto, "minutos e", total_segundos, "segundos.")