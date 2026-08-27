# antes de executar o código abaixo, é necessário importar
# o pacote pycoin no python. para isso, basta
# executar o comando abaixo.
#
# pip install pycoin

from pycoin.ecdsa.secp256k1 import secp256k1_generator
import hashlib, secrets

def sha3_256Hash(msg):
    hashBytes = hashlib.sha3_256(msg.encode("utf8")).digest()
    return int.from_bytes(hashBytes, byteorder="big")

def signECDSAsecp256k1(msg, privKey):
    msgHash = sha3_256Hash(msg)
    signature = secp256k1_generator.sign(privKey, msgHash)
    return signature

def verifyECDSAsecp256k1(msg, signature, pubKey):
    msgHash = sha3_256Hash(msg)
    valid = secp256k1_generator.verify(pubKey, msgHash, signature)
    return valid

# assinatura da mensagem utilizando ECDSA utilizando a curva secp256k1 e hash SHA3-256
msg = "Message for ECDSA signing"
# O zero não é uma chave privada ECDSA válida.
privKey = secrets.randbelow(secp256k1_generator.order() - 1) + 1
signature = signECDSAsecp256k1(msg, privKey)
print("Message:", msg)
print("Private key (demo only):", hex(privKey))
print("Signature: r=" + hex(signature[0]) + ", s=" + hex(signature[1]))

# verificando a assinatura utilizando ECDSA utilizando secp256k1 e hash SHA3-256
pub_key_point = secp256k1_generator * privKey
pubKey = (pub_key_point[0], pub_key_point[1])
valid = verifyECDSAsecp256k1(msg, signature, pubKey)
print("\nMessage:", msg)
print("Public key: (" + hex(pubKey[0]) + ", " + hex(pubKey[1]) + ")")
print("Signature valid?", valid)

# verificando a assinatura utilizando ECDSA utilizando secp256k1 e hash SHA3-256
msg = "Tampered message"
valid = verifyECDSAsecp256k1(msg, signature, pubKey)
print("\nMessage:", msg)
print("Signature (tampered msg) valid?", valid)
