# importando bibliotecas
import hashlib, hmac, binascii

# calcular o hmac da string
mac = hmac.new(b'key', b'some msg', hashlib.sha256).digest()

# exibir o resultado
print(binascii.hexlify(mac))