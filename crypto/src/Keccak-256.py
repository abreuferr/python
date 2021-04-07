# Para calcular o hash Keccak-256, é necessário importar uma bilbioteca
# não padrão Python. Para isso, é necessário executar o comando abaixo.
#
# pip install pycryptodome

# importando funcao crypto.hash da biblioteca keccak 
from Crypto.Hash import keccak

# importando a biblioteca
import binascii

# calcular o hash keccak256 de uma string 
keccak256 = keccak.new(data=b'hello', digest_bits=256).digest()

# exibir o resultado
print("Keccak256:", binascii.hexlify(keccak256))