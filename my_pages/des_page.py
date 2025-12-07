# my_pages/des_page.py
import streamlit as st
from pyDes import des, ECB, PAD_PKCS5

# ---------------- History Helper ---------------- #
def add_to_history(algo, action, input_text, output_text):
    if "history" not in st.session_state:
        st.session_state["history"] = []
    st.session_state["history"].append({
        "algo": algo,       # "DES"
        "action": action,   # "Encryption" أو "Decryption"
        "input": input_text,
        "output": output_text
    })



# ---------- DES Encryption ----------
def des_encrypt(plaintext, key):
    if len(key) != 8:
        return "❌ Key must be exactly 8 characters"
    d = des(key, ECB, padmode=PAD_PKCS5)
    encrypted = d.encrypt(plaintext)
    return encrypted.hex()

# ---------- DES Decryption ----------
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
    st.markdown('<h1 style="color:#a8c0ff; font-weight:700; margin-bottom:25px;">DES Encryption / Decryption</h1>', unsafe_allow_html=True)

    text_input = st.text_input("Plaintext / Cipher (HEX)", key="des_text")
    key_input = st.text_input("Key (8 chars)", key="des_key")

    result_e = ""
    result_d = ""

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Encrypt", key="des_enc_btn"):
            if not text_input or not key_input:
                st.warning("⚠️ Please enter both text and key.")
            else:
                result_e = des_encrypt(text_input.strip(), key_input.strip())
                add_to_history("DES", "Encryption", text_input.strip(), result_e)

    with col2:
        if st.button("Decrypt", key="des_dec_btn"):
            if not text_input or not key_input:
                st.warning("⚠️ Please enter both text and key.")
            else:
                result_d = des_decrypt(text_input.strip(), key_input.strip())
                add_to_history("DES", "Decryption", text_input.strip(), result_d)

    if result_e:
        st.subheader("Encryption")
        st.code(result_e)
    if result_d:
        st.subheader("Decryption")
        st.code(result_d)


