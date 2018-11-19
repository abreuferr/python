# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : comparacao entre string

x = "teoria"
y = "pratica"
z = "teoria"

fruta1 = "Banana"
fruta2 = "banana"

x == y # retorna False
x != y # retorna True
x == z # retorna True
x is z # retorna True
x > y # retorna True (codigo Unicode)

lower(fruta1) == lower(fruta2) # retorna True