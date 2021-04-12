# antes de executar o código abaixo, é necessário importar
# o pacote pycryptodome no python. para isso, basta
# executar o comando abaixo.
#
# pip install pycryptodome

# importando bilbioteca
from Crypto.PublicKey import RSA
from hashlib import sha512

#
# geracao das chaves publica e privada
#

# gerando par de chaves RSA de 1024 bits
keyPair = RSA.generate(bits=1024)

# exibindo a chave publica e a chave privada
print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")

# 
# assinatura do hash da mensagem
#

# mensagem a ser assinada
msg = b'A message for signing'

# gerando o hash, sha512, da mensagem
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')

# chave privada {n, d}
#
# pow(x, y, z) is equal to xy % z
#
#    x - a number, the base
#    y - a number, the exponent
#    z (optional) - a number, used for modulus
#
# s = h^d (mod n)
signature = pow(hash, keyPair.d, keyPair.n)

# exibir a assinatura da mensagem
print("Signature:", hex(signature))

#
# verificacao da assinatura
#

# mensagem qye sera verificada
msg = b'A message for signing (tampered)'

# geracao do hash da mensagem acima
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')

# gerando o hash da assinatura
hashFromSignature = pow(signature, keyPair.e, keyPair.n)

# exibindo a validade ou nao da assinatura
print("Signature valid:", hash == hashFromSignature)