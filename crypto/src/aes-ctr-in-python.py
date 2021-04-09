# antes de executar o código abaixo, é necessário importar
# os pacotes pyaes e pbkdf2 no python. para isso, basta
# executar o comando abaixo.
#
# pip install pyaes e pbkdf2

# importando biblioteca
import pyaes, pbkdf2, binascii, os, secrets

# Derivando a chave de criptografia 256-bit AES baseada na senha
password = "s3cr3t*c0d3" # definindo a senha
passwordSalt = os.urandom(16) # definindo o valor do salt
key = pbkdf2.pbkdf2(password, passwordSalt).read(32) # calculando a chave
print('AES encryption key:', binascii.hexlify(key)) # exibindo a chave