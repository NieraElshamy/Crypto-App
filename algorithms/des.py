from pyDes import des, ECB, PAD_PKCS5

# دالة التشفير
def des_encryptt(plaintext, key):
    if len(key) != 8:
        raise ValueError("Key must be exactly 8 characters")
    cipher = des(key, ECB, padmode=PAD_PKCS5)
    encrypted = cipher.encrypt(plaintext)
    return encrypted.hex()  # رجعنا النص المتشفر بالهيكسا

# دالة فك التشفير
def des_decryptt(ciphertext_hex, key):
    if len(key) != 8:
        raise ValueError("Key must be exactly 8 characters")
    cipher = des(key, ECB, padmode=PAD_PKCS5)
    encrypted_bytes = bytes.fromhex(ciphertext_hex)
    decrypted = cipher.decrypt(encrypted_bytes)
    return decrypted.decode()  # النص الأصلي يرجع
