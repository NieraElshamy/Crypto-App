import streamlit as st

# ---------------- Affine Cipher Functions ----------------
def affine_encrypt(p, a, b):
    return ''.join(
        chr(((a * (ord(ch) - 97) + b) % 26) + 97)
        for ch in p.lower() if ch.isalpha()
    )

def affine_decrypt(c, a, b):
    # حساب modular inverse للـ a
    inv = None
    for x in range(26):
        if (a * x) % 26 == 1:
            inv = x
            break
    if inv is None:
        raise ValueError("a has no modular inverse modulo 26")
    return ''.join(
        chr(((inv * (ord(ch) - 97 - b)) % 26) + 97)
        for ch in c.lower() if ch.isalpha()
    )

# ---------------- History Helper ----------------
def add_to_history(algo, action, input_text, output_text):
    if "history" not in st.session_state:
        st.session_state["history"] = []
    st.session_state["history"].append({
        "algo": algo,       # "Affine"
        "action": action,   # "Encryption" أو "Decryption"
        "input": input_text,
        "output": output_text
    })

# ---------------- Affine Page ----------------
def show_affine_page():
    st.title("Affine Cipher 🧩")

    # ---------- Encryption ----------
    st.subheader("Encryption")
    text = st.text_input("Plaintext", key="affine_plain")
    a = st.number_input("Key a", min_value=1, max_value=25, step=1, key="affine_a_enc")
    b = st.number_input("Key b", min_value=0, max_value=25, step=1, key="affine_b_enc")

    if st.button("Encrypt", key="affine_enc_btn"):
        try:
            result = affine_encrypt(text, a, b)
            st.success(result)
            add_to_history("Affine", "Encryption", text, result)
        except Exception as e:
            st.error(f"Error: {str(e)}")

    # ---------- Decryption ----------
    st.subheader("Decryption")
    text2 = st.text_input("Ciphertext", key="affine_ciph")
    a2 = st.number_input("Key a (again)", min_value=1, max_value=25, step=1, key="affine_a_dec")
    b2 = st.number_input("Key b (again)", min_value=0, max_value=25, step=1, key="affine_b_dec")

    if st.button("Decrypt", key="affine_dec_btn"):
        try:
            result2 = affine_decrypt(text2, a2, b2)
            st.success(result2)
            add_to_history("Affine", "Decryption", text2, result2)
        except Exception as e:
            st.error(f"Error: {str(e)}")
