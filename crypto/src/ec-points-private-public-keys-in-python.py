# antes de executar o código abaixo, é necessário importar
# o pacote tinyec no python. para isso, basta
# executar o comando abaixo.
#
# pip install tinyec

# importando biblioteca
from tinyec import registry
import secrets

# Exemplo histórico: secp192r1 oferece apenas cerca de 96 bits de segurança.
# Para novos sistemas, prefira curvas de 256 bits em uma biblioteca de produção.
# tinyec é utilizado apenas para visualizar a aritmética de pontos.
# definindo o algoritmo a ser utilizado
curve = registry.get_curve('secp192r1')

# chave privada e a chave publica
privKey = secrets.randbelow(curve.field.n)
pubKey = privKey * curve.g

# exibindo a chave privada e chave publica
# A impressão da chave serve apenas para acompanhar este exemplo efêmero.
print("private key (demo only):", privKey)
print("public key:", pubKey)
