# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : Conceitos teóricos do python

# funcao peso_altura
def peso_altura():
    return 65, 1.80

# funcao pagamento semanal
def pagamento_semanal(valor_hora, numero_hora):
    assert valor_hora >= 0 and numero_hora > 0 # verificar os valores inseridos
    return valor_hora * numero_hora # calcula e retorna o resultado

a, b = 10, 20 # atribuindo valor a variavel
print(a) # exibindo o conteudo da variave a
print(b) # exibindo o conteudo da variavel b

peso, altura = peso_altura() # atribuir valor a variavel atraves de uma funcao
print(peso) # exibindo o conteudo da variaval peso
print(altura) # exibindo o conteudo da variavel altura

a, b = 10, 20 # atribuindo valor a variavel
a, b = b, a # o conteudo das variaveis sao trocados
print(a) # exibindo o conteudo da variave a (20)
print(b) # exibindo o conteudo da variavel b (10)

a = 10 # atribuindo valor a uma variavel
a += 10 # incrementando a variavel em 10
a *= 2 # incrementa o valor da variavel em * 2 (20)
a **=2 # **= representa elevado
print(a) # exibindo o conteudo da variavel a

valor = pagamento_semanal(100, 36) # chamando funcao passando valores
print(valor) # exibindo o conteudo da variavel valor

valor = pagamento_semanal(100, -1)  # chamando funcao passando valores, vai retornar erro