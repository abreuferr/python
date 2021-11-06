# antes de executar o código abaixo, é necessário importar
# o pacote pyDHE no python. para isso, basta
# executar o comando abaixo.
#
# pip install pyDHE

# importando biblioteca
import pyDHE

alice = pyDHE.new(group=18)
alicePubKey = alice.getPublicKey() # gerando chave publica da Alice, chave publica de 2048 bits
print("Alice public key:", hex(alicePubKey)) # exibindo chave publica da alice

bob = pyDHE.new(group=18)
bobPubKey = bob.getPublicKey() # gerando chave prublica do Bob, chave publica de 2048 bits
print("Bob public key:", hex(bobPubKey)) # exibindo a chave publica do Bob

# ambas as chaves publicas sao trocadas via internet
print("Now exchange the public keys (e.g. through Internet)")

# Baseada na chave publica de Bob, Alice calcula a chave secreta de 2048 bits
aliceSharedKey = alice.update(bobPubKey)
print("Alice shared key:", hex(aliceSharedKey))

# Baseada na chave publica de Alice, Bob calcula a chave secreta de 2048 bits
bobSharedKey = bob.update(alicePubKey)
print("Bob shared key:", hex(bobSharedKey))

# A chave secreta de Bob e Alice sao iguais.
print("Equal shared keys:", aliceSharedKey == bobSharedKey)