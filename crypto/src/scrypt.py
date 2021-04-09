# antes de executar o código abaixo, é necessário importar
# o pacote backports.pbkdf2 no python. para isso, basta
# executar o comando abaixo.
#
# pip install scrypt

# importando a biblioteca pyscrypt
import pyscrypt

# definicao as variaveis
salt = b'aa1f2d3f4d23ac44e9c5a6c3d8f9ee8c'
passwd = b'qwerty$Sw0rD~7'

# calculando a derivacao da chave
# password (bytes sequence)
# salt (bytes sequence)
# iterations count
# block size for each iteration
# parallelism factor
# key length (number of bytes for the derived key).
key = pyscrypt.hash(passwd, salt, 2048, 8, 1, 32)

# exibindo o resultado
print("Derived key:", key.hex())