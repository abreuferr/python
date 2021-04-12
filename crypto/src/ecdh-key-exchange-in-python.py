# antes de executar o código abaixo, é necessário importar
# o pacote tinyec no python. para isso, basta
# executar o comando abaixo.
#
# pip install tinyec

# importando biblioteca
from tinyec import registry
import secrets

def compress(pubKey):
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]

# definicao do algoritmo de ECC que sera utilizado - 256 bits
curve = registry.get_curve('brainpoolP256r1')

# calculando as chaves publicas e privadas de Alice
alicePrivKey = secrets.randbelow(curve.field.n) # 256 bits
alicePubKey = alicePrivKey * curve.g # 257 bits

# exibindo a chave publica de Alice
print("Alice public key:", compress(alicePubKey))

# caclculando as chaves publicas e privadas de Bob
bobPrivKey = secrets.randbelow(curve.field.n) # 256 bits
bobPubKey = bobPrivKey * curve.g # 257 bits

# exibindo a chave publica de Bob
print("Bob public key:", compress(bobPubKey))

print("Now exchange the public keys (e.g. through Internet)")

# calculando a chaveCompartilhamento
aliceSharedKey = alicePrivKey * bobPubKey
print("Alice shared key:", compress(aliceSharedKey))

# calculando a chaveCompartilhamento
bobSharedKey = bobPrivKey * alicePubKey
print("Bob shared key:", compress(bobSharedKey))

# se ambas as chaves chaveCompartilhamento sao iguais
print("Equal shared keys:", aliceSharedKey == bobSharedKey)