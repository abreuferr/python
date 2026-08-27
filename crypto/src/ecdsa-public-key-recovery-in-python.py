"""Demonstra recuperação de chave pública a partir de uma assinatura ECDSA."""

import hashlib
import secrets

from pycoin.ecdsa.secp256k1 import secp256k1_generator


def sha3_256_hash(msg):
    """Converte a mensagem em inteiro, como requerido pela API do pycoin."""
    return int.from_bytes(hashlib.sha3_256(msg.encode("utf-8")).digest(), "big")


def recover_pub_keys_from_signature(msg, signature):
    msg_hash = sha3_256_hash(msg)
    return secp256k1_generator.possible_public_pairs_for_signature(msg_hash, signature)


def main():
    msg = "Message for ECDSA signing"
    # O zero é inválido como escalar privado; portanto o intervalo é 1..n-1.
    private_key = secrets.randbelow(secp256k1_generator.order() - 1) + 1
    signature = secp256k1_generator.sign(private_key, sha3_256_hash(msg))
    public_key_point = secp256k1_generator * private_key
    public_key = (public_key_point[0], public_key_point[1])
    recovered_pub_keys = recover_pub_keys_from_signature(msg, signature)

    print("Message:", msg)
    print("Signature: r=" + hex(signature[0]) + ", s=" + hex(signature[1]))
    print("Original public key: (" + hex(public_key[0]) + ", " + hex(public_key[1]) + ")")
    for pk in recovered_pub_keys:
        print("Recovered public key: (" + hex(pk[0]) + ", " + hex(pk[1]) + ")")
    print("Original key recovered?", public_key in recovered_pub_keys)


if __name__ == "__main__":
    main()
