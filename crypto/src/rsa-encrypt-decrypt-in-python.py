# antes de executar o código abaixo, é necessário importar
# o pacote pycryptodome no python. para isso, basta
# executar o comando abaixo.
#
# pip install pycryptodome

# importando bilbioteca
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# gerando o par de chaves
keyPair = RSA.generate(3072)

# chave publica
pubKey = keyPair.publickey()

# string a ser criptografada
msg = b'A message for encryption'

# criptografando a string
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)

# exibindo a string criptografada
print("Encrypted:", binascii.hexlify(encrypted))

# descriptografa a string
decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)

# exibir a string descriptografada
print('Decrypted:', decrypted)