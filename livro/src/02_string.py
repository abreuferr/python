# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : variavel do tipo string.

#
# string.
# 
# criar a variavel "texto" do tipo string e definir o seu conteudo.
texto = "esse texto eh considerado uma string."
# imprimindo a variavel.
print(texto)

#
# title() - Formato Titulo
# 
# variavel "nome".
nome = "caio abreu ferreira"
# imprimindo a variavel.
print(nome.title())

#
# upper() - maiuscula
# lower() - minuscula
# 
# variavel "nome".
nome = "Caio Abreu Ferreira"
# imprimindo a variavel.
print(nome.upper())
print(nome.lower())

#
# concatenando string
# 
# definindo variavel
primeiro_nome = "caio"
ultimo_nome = "ferreira"
# concatenando as variaveis
nome_completo = primeiro_nome + " " + ultimo_nome
print(nome_completo)
# concatenando as variaveis e capslock na variavel.
mensagem = "Ola, " + nome_completo.title() + "!!!"
print(mensagem)

#
# \t - tabulacao
# 
# definindo variavel
texto = "\tesse texto eh considerado uma string."
# imprimindo a variavel.
print(texto)

#
# \n - quebra de linha 
# \t - tabulacao
# 
# definindo variavel
texto = "Linguagem de programacao: \n\t- Python\n\t- C\n\t- Objective-C"
# imprimindo variavel
print(texto)

#
# rstrip() - remover espaco em branco no final da string.
# lstrip() - remover espaco em branco no comeco da string.
# sstrip() - remover espaco em branco no comeco e no final da string.
# 
# definindo variavel
texto = " caio abreu ferreira "
sem_espaco_final = texto.rstrip()
sem_espaco_comeco = texto.ltrip()
sem_espaco_comeco_final = texto.strip()
# imprimindo variavel
print(sem_espaco_final)
print(sem_espaco_comeco)
print(sem_espaco_comeco_final)