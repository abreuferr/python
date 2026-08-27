"""Assinatura e verificação Ed25519 com uma API mantida."""

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey


priv_key = Ed25519PrivateKey.generate()
pub_key = priv_key.public_key()

# A chave exibida é efêmera e serve somente para estudo. Não registre segredos.
private_bytes = priv_key.private_bytes(
    serialization.Encoding.Raw,
    serialization.PrivateFormat.Raw,
    serialization.NoEncryption(),
)
public_bytes = pub_key.public_bytes(
    serialization.Encoding.Raw,
    serialization.PublicFormat.Raw,
)
print("Private key (demo only, 32 bytes):", private_bytes.hex())
print("Public key (32 bytes):", public_bytes.hex())

msg = b'Message for Ed25519 signing'
signature = priv_key.sign(msg)
print("Signature (64 bytes):", signature.hex())

try:
    pub_key.verify(signature, msg)
    print("The signature is valid.")
except InvalidSignature:
    print("Invalid signature!")
