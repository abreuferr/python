# antes de executar o código abaixo, é necessário importar
# o pacote argon2_cffi no python. para isso, basta
# executar o comando abaixo.
#
# pip install argon2_cffi

# O arquivo não se chama ``argon2.py`` para não sombrear o pacote importado.
import argon2
import binascii

# O salt fixo é somente um valor didático para a derivação raw.
raw_hash = argon2.low_level.hash_secret_raw(
    time_cost=16,
    memory_cost=2**15,
    parallelism=2,
    hash_len=32,
    secret=b'password',
    salt=b'some salt',
    type=argon2.low_level.Type.ID,
)

print("Argon2 raw hash:", binascii.hexlify(raw_hash))

argon2_hasher = argon2.PasswordHasher(
    time_cost=16, memory_cost=2**15, parallelism=2, hash_len=32, salt_len=16)
password_hash = argon2_hasher.hash("password")
print("Argon2 hash (random salt):", password_hash)

verify_valid = argon2_hasher.verify(password_hash, "password")
print("Argon2 verify (correct password):", verify_valid)

try:
    argon2_hasher.verify(password_hash, "wrong123")
except argon2.exceptions.VerifyMismatchError:
    print("Argon2 verify (incorrect password):", False)
