# algorithms/affine_algo.py

# ======================= Build Custom Alphabet ===========================
def build_alphabet():
    english_lower = [chr(i) for i in range(97, 123)]       # a-z
    english_upper = [chr(i) for i in range(65, 91)]        # A-Z
    digits = [str(i) for i in range(10)]                   # 0-9
    arabic = [chr(i) for i in range(0x0621, 0x064B)]       # الحروف العربية

    return english_lower + english_upper + digits + arabic


ALPHABET = build_alphabet()
N = len(ALPHABET)
# ========================================================================


# ---------------------- Affine Encrypt ----------------------------------
def affine_encrypt(text, a, b):
    encrypted = ""

    for ch in text:
        if ch in ALPHABET:
            idx = ALPHABET.index(ch)
            new_idx = (a * idx + b) % N
            encrypted += ALPHABET[new_idx]
        else:
            encrypted += ch   # رمز غير موجود → نسيبه

    return encrypted


# ---------------------- Find Modular Inverse -----------------------------
def mod_inverse(a, m):
    for x in range(m):
        if (a * x) % m == 1:
            return x
    return None


# ---------------------- Affine Decrypt ----------------------------------
def affine_decrypt(cipher, a, b):
    inv = mod_inverse(a, N)
    if inv is None:
        raise ValueError("Key 'a' has no modular inverse modulo alphabet size")

    decrypted = ""

    for ch in cipher:
        if ch in ALPHABET:
            idx = ALPHABET.index(ch)
            new_idx = (inv * (idx - b)) % N
            decrypted += ALPHABET[new_idx]
        else:
            decrypted += ch

    return decrypted
