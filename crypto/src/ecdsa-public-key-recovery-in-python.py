from pycoin.ecdsa import possible_public_pairs_for_signature

def recoverPubKeyFromSignature(msg, signature):
    msgHash = sha3_256Hash(msg)
    recoveredPubKeys = possible_public_pairs_for_signature(
        generator_secp256k1, msgHash, signature)
    return recoveredPubKeys

msg = "Message for ECDSA signing"
recoveredPubKeys = recoverPubKeyFromSignature(msg, signature)
print("\nMessage:", msg)
print("Signature: r=" + hex(signature[0]) + ", s=" + hex(signature[1]))
for pk in recoveredPubKeys:
    print("Recovered public key from signature: (" +
          hex(pk[0]) + ", " + hex(pk[1]) + ")")