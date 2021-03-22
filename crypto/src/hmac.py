# importando bibliotecas
import hashlib, hmac, binascii

# funcao que ira calcular o hmac.
# recebe como paramentro uma chave e a mensagem a ser criptografada
def hmac_sha256(key, msg):
  return hmac.new(key, msg, hashlib.sha256).digest()

# chave utilizada pelo hmaca
key = b"12345"

# mensagem que sera crida o hmac
msg = b"sample message"

# exibe o HMAC da mensagem
print(binascii.hexlify(hmac_sha256(key, msg)))