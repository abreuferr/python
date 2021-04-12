# importando as bilbiotecas necessarias
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii

# gerando o par de chaves RSA de 1024-bit
keyPair = RSA.generate(bits=1024)
pubKey = keyPair.publickey()

# Assinando a mensagem utilizando o esquema PKCS#1 v1.5 (RSASP1)
msg = b'Message for RSA signing' # mensagem a ser assinada
hash = SHA256.new(msg) # gerando o hash da mensagem
signer = PKCS115_SigScheme(keyPair) # definindo qual eh o esquema a ser utilizado
signature = signer.sign(hash) # assinando a mensagem
print("Signature:", binascii.hexlify(signature)) # exibindo a assinatura da mensagem

# verificando se a assinatura eh valida ou nao, PKCS#1 v1.5 (RSAVP1)
msg = b'Message for RSA signing'
hash = SHA256.new(msg)
verifier = PKCS115_SigScheme(pubKey)
try:
    verifier.verify(hash, signature)
    print("Signature is valid.")
except:
    print("Signature is invalid.")

# verificando se a assinatura eh valida ou nao, PKCS#1 v1.5 (RSAVP1)
msg = b'A tampered message'
hash = SHA256.new(msg)
verifier = PKCS115_SigScheme(pubKey)
try:
    verifier.verify(hash, signature)
    print("Signature is valid.")
except:
    print("Signature is invalid.")