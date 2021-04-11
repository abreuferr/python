# antes de executar o código abaixo, é necessário importar
# o pacote backports.pbkdf2 no python. para isso, basta
# executar o comando abaixo.
#
# pip install backports.pbkdf2

# importando biblioteca
import os, binascii

# importando biblioteca python externa, pip install backports.pbkdf2
from backports.pbkdf2 import pbkdf2_hmac

# definindo os valor das variaveis
salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
passwd = "p@$Sw0rD~1".encode("utf8")

# calculando o valor da derivada da chave
# key = pbkdf2_hmac(hash function, password, salt, interactions, key lenght)
key = pbkdf2_hmac("sha256", passwd, salt, 5000, 32)

# exibindo a derivada da chave
print("Derived key:", binascii.hexlify(key))