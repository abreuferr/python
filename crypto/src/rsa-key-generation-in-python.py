# antes de executar o código abaixo, é necessário importar
# o pacote pycryptodome no python. para isso, basta
# executar o comando abaixo.
#
# pip install pycryptodome

# importando bilbioteca
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# gerando par de chaves RSA de tamanho 3072
keyPair = RSA.generate(3072)

# calculando a chave publica
pubKey = keyPair.publickey()

# exibe a chave publica no formato hexadecimal
# - par {n, e} = chave publica
# exibe os valores "n" e "e"
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")

# exibe a chave no formato PKCS#8 PEM ASN.1
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

# exibe a chave privada no formato hexadecimal
# - para {n, d} = chave privada
# exibe os valores "n" e "d"
print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")

# exibe a chave privada no formato PKCS#8 PEM ASN.1
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))