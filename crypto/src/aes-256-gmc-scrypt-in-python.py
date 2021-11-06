# antes de executar o código abaixo, é necessário importar
# o pacote pycryptodome e scrypt no python. para isso, basta
# executar o comando abaixo.
#
# pip install pycryptodome
# pip install scrypt

# importando bilbiotecas
from Crypto.Cipher import AES
import scrypt, os, binascii

# funcao utilizada para criptografar uma string
def encrypt_AES_GCM(msg, password):
    kdfSalt = os.urandom(16) # KDF salt
    secretKey = scrypt.hash(password, kdfSalt, N=16384, r=8, p=1, buflen=32) # chave baseada no hash Scrypt KDF
    aesCipher = AES.new(secretKey, AES.MODE_GCM) # criptografia da string
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (kdfSalt, ciphertext, aesCipher.nonce, authTag)

# funcao utilizada para descriptografar uma string
def decrypt_AES_GCM(encryptedMsg, password):
    (kdfSalt, ciphertext, nonce, authTag) = encryptedMsg
    secretKey = scrypt.hash(password, kdfSalt, N=16384, r=8, p=1, buflen=32)
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext

# string a ser criptografada
msg = b'Message for AES-256-GCM + Scrypt encryption'

# senha
password = b's3kr3tp4ssw0rd'

# chamada da funcao que ira criptografar a string
encryptedMsg = encrypt_AES_GCM(msg, password)
print("encryptedMsg", {
    'kdfSalt': binascii.hexlify(encryptedMsg[0]), # salt
    'ciphertext': binascii.hexlify(encryptedMsg[1]), # string cifrada
    'aesIV': binascii.hexlify(encryptedMsg[2]), # vetor de inicializacao
    'authTag': binascii.hexlify(encryptedMsg[3]) # MAC - message authentication code de 128 bits, 32 hex
})

# chamada da funcao que ira descriptografar a string
decryptedMsg = decrypt_AES_GCM(encryptedMsg, password)
print("decryptedMsg", decryptedMsg)