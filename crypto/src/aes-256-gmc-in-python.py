# antes de executar o código abaixo, é necessário importar
# o pacote pycryptodome no python. para isso, basta
# executar o comando abaixo.
#
# pip install pycryptodome

# importando 
from Crypto.Cipher import AES
import binascii, os

# funcao utilizada para criptografar os dados
def encrypt_AES_GCM(msg, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)

# funcao utilizada para descriptografar os dados
def decrypt_AES_GCM(encryptedMsg, secretKey):
    (ciphertext, nonce, authTag) = encryptedMsg
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext

secretKey = os.urandom(32)  # chave de 256-bit gerada de forma ramdomica
print("Encryption key:", binascii.hexlify(secretKey))

# string que sera critpografada
msg = b'Message for AES-256-GCM + Scrypt encryption'

# chamada da funcao que ira criptografar a string de ados
encryptedMsg = encrypt_AES_GCM(msg, secretKey)

print("encryptedMsg", {
    'ciphertext': binascii.hexlify(encryptedMsg[0]), # string criptografada
    'aesIV': binascii.hexlify(encryptedMsg[1]), # vetor de inicializacao de 128 bits, 32 hex
    'authTag': binascii.hexlify(encryptedMsg[2]) # MAC - message authentication code de 128 bits, 32 hex
})

# chamada da funcao que ira descriptografar a string
decryptedMsg = decrypt_AES_GCM(encryptedMsg, secretKey)
print("decryptedMsg", decryptedMsg)