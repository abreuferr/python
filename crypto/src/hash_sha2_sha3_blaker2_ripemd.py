# importando bibliotecas
import hashlib, binascii

# definicao das variaveis
text = 'hello'              # texto que sera gerado o hash
data = text.encode("utf8")  # codificando o texto no formato utf8

# gerando o hash sha256
sha256hash = hashlib.sha256(data).digest()
# exibindo o resultado em formato hexadecimal.
print("SHA-256:   ", binascii.hexlify(sha256hash))

sha3_256 = hashlib.sha3_256(data).digest()
print("SHA3-256:  ", binascii.hexlify(sha3_256))

blake2s = hashlib.new('blake2s', data).digest()
print("BLAKE2s:   ", binascii.hexlify(blake2s))

ripemd160 = hashlib.new('ripemd160', data).digest()
print("RIPEMD-160:", binascii.hexlify(ripemd160))