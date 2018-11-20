# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : o programa deve contar quantas letras
''' 
Escreva a função conta_letras(frase, contar="vogais"), que 
recebe como primeiro parâmetro uma string contendo uma frase 
e como segundo parâmetro uma outra string. Este segundo parâmetro 
deve ser opcional.

Quando o segundo parâmetro for definido como "vogais", a função 
deve devolver o numero de vogais presentes na frase. Quando ele 
for definido como "consoantes", a função deve devolver o número 
de consoantes presentes na frase. Se este parâmetro não for passado 
para a função, deve-se assumir o valor "vogais" para o parâmetro.
'''

# funcao conta_letras
def conta_letras(frase, tipo = "vogais"):
    total = 0

    # normalizando a frase
    frase_lower = frase.lower() # todos os caracteres em caixa baixa
    frase_normalizada = frase_lower.replace(" ", "") # remover os espaços

    if tipo == "vogais":
        vogal_a = frase_normalizada.count("a")
        vogal_e = frase_normalizada.count("e")
        vogal_i = frase_normalizada.count("i")
        vogal_o = frase_normalizada.count("o")
        vogal_u = frase_normalizada.count("u")
        total = vogal_a + vogal_e + vogal_i + vogal_o + vogal_u

    if tipo != "vogais":
        vogal_a = frase_normalizada.count("a")
        vogal_e = frase_normalizada.count("e")
        vogal_i = frase_normalizada.count("i")
        vogal_o = frase_normalizada.count("o")
        vogal_u = frase_normalizada.count("u")
        total = len(frase_normalizada) - (vogal_a + vogal_e + vogal_i + vogal_o + vogal_u)

    return total

# main()
conta_letras('programamos em python')# deve devolver 6

conta_letras('programamos em python', 'vogais')# deve devolver 6

conta_letras('programamos em python', 'consoantes')# deve devolver 13