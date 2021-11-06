# antes de executar o código abaixo, é necessário importar
# os pacotes pyaes e pbkdf2 no python. para isso, basta
# executar o comando abaixo.
#
# pip install pyaes e pbkdf2

# importando biblioteca
import pyaes, pbkdf2, binascii, os, secrets

# Derivando a chave de criptografia 256-bit AES baseada na senha
password = "s3cr3t*c0d3" # definindo a senha
passwordSalt = os.urandom(16) # definindo o valor do salt
key = pbkdf2.PBKDF2(password, passwordSalt).read(32) # calculando a chave
print('AES encryption key:', binascii.hexlify(key)) # exibindo a chave

# criptografar um texto com uma chave abaixo:
# ciphertext = AES-256-CTR-Encrypt(plaintext, key, iv)

# vetor de inicializacao
iv = secrets.randbits(256)

# texto a ser cifrado
plaintext = "Text for encryption"

# chave de criptografia
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))

# cifrando o texto
ciphertext = aes.encrypt(plaintext)

# exibindo o texto cifrado
print('Encrypted:', binascii.hexlify(ciphertext))

# descriptografa o texto previamente criptografado com a chave
# plaintext = AES-256-CTR-Decrypt(ciphertext, key, iv)

aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))

# descriptografando o dado
decrypted = aes.decrypt(ciphertext)

# exibindo a mensagem original.
print('Decrypted:', decrypted)