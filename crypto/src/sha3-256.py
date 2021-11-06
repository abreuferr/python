# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : geracao do hash sha3-256

# importando bibliotecas
import hashlib, binascii

# definicao do conteudo da variavel sha3_256
sha3_256hash = hashlib.sha3_256(b'hello').digest()

# exibir o  hash da palavra hello
print("SHA3-256('hello') =", binascii.hexlify(sha3_256hash))