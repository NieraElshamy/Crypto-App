import streamlit as st
from pyDes import des, ECB, PAD_PKCS5


# ---------- Encryption ----------
def des_encrypt(plaintext, key):
    if len(key) != 8:
        return "❌ Key must be exactly 8 characters"
    d = des(key, ECB, padmode=PAD_PKCS5)
    encrypted = d.encrypt(plaintext)
    return encrypted.hex()

# ---------- Decryption ----------
from pyDes import des, ECB, PAD_PKCS5

# ---------- Decryption ----------
def des_decrypt(cipher_hex, key):
    if len(key) != 8:
        return "❌ Key must be exactly 8 characters"
    try:
        cipher_bytes = bytes.fromhex(cipher_hex.strip())
    except ValueError:
        return "❌ Input must be HEX"

    try:
        d = des(key, ECB, padmode=PAD_PKCS5)
        decrypted_bytes = d.decrypt(cipher_bytes)
        decrypted_text = decrypted_bytes.decode(errors='ignore')
        return decrypted_text
    except Exception:
        return "❌ Failed: Decryption error (check key or ciphertext)"

# ---------- Streamlit Page ----------
def show_des_page():
    st.title("DES Encryption / Decryption")
    text_input = st.text_input("Plaintext / Cipher (HEX)")
    key_input = st.text_input("Key (8 chars)")
    result_e = "" 
    result_d= "" 
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Encrypt"):
            if not text_input or not key_input:
                st.warning("⚠️ Please enter both text and key.")
            else:
                result_e = des_encrypt(text_input.strip(), key_input.strip())
    with col2:
        if st.button("Decrypt"):
            if not text_input or not key_input:
                st.warning("⚠️ Please enter both text and key.")
            else:
                result_d = des_decrypt(text_input.strip(), key_input.strip())
    if result_e:
      st.subheader("Encryption")
      st.code(result_e)
    if result_d:
      st.subheader("Decryption")
      st.code(result_d)
