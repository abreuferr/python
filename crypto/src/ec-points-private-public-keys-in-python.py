# antes de executar o código abaixo, é necessário importar
# o pacote tinyec no python. para isso, basta
# executar o comando abaixo.
#
# pip install tinyec

# importando biblioteca
from tinyec import registry
import secrets

# definindo o algoritmo a ser utilizado
curve = registry.get_curve('secp192r1')

# chave privada e a chave publica
privKey = secrets.randbelow(curve.field.n)
pubKey = privKey * curve.g

# exibindo a chave privada e chave publica
print("private key:", privKey)
print("public key:", pubKey)