import streamlit as st

# ---------------- User's row transposition functions (kept mostly as you wrote) ----------------
def row_transposition_encryption(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()

    key_list = [int(k) for k in str(key)]
    n_col = len(key_list)

    # حساب عدد الصفوف
    n_row = len(plaintext) // n_col
    if len(plaintext) % n_col != 0:
        n_row += 1

    # بناء المصفوفة
    matrix = [['X' for _ in range(n_col)] for _ in range(n_row)]
    idx = 0
    for r in range(n_row):
        for c in range(n_col):
            if idx < len(plaintext):
                matrix[r][c] = plaintext[idx]
                idx += 1

    # ترتيب الأعمدة حسب key
    col_order = sorted(range(len(key_list)), key=lambda i: key_list[i])

    # استخراج النص المشفر
    cipher = ""
    for col in col_order:
        for r in range(n_row):
            cipher += matrix[r][col]

    return cipher
def row_transposition_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key_list = [int(k) for k in str(key)]

    n_col = len(key_list)
    n_row = len(ciphertext) // n_col

    # تجهيز مصفوفة فارغة
    matrix = [['' for _ in range(n_col)] for _ in range(n_row)]

    # ترتيب الأعمدة حسب key
    col_order = sorted(range(len(key_list)), key=lambda i: key_list[i])

    # ملء الأعمدة من النص المشفر
    idx = 0
    for col in col_order:
        for r in range(n_row):
            matrix[r][col] = ciphertext[idx]
            idx += 1

    # قراءة الصفوف لإعادة النص
    plaintext = ""
    for r in range(n_row):
        for c in range(n_col):
            plaintext += matrix[r][c]

    return plaintext

# ---------------- Streamlit UI ----------------
def show_row_cipher_page():
    st.set_page_config(page_title="Row Transposition Cipher", layout="centered")

    # ---------- Custom CSS ----------
    st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #0b0c10, #1c1f2a);
        color: #e0e0e0;
        font-family: 'Inter', sans-serif;
    }
    .float-circle {
        position: absolute;
        border-radius: 50%;
        background: rgba(168,192,255,0.08);
        animation: floatAnim 8s ease-in-out infinite;
    }
    .float-circle:nth-child(1){ top: 30px; left: 20%; width: 80px; height: 80px;}
    .float-circle:nth-child(2){ top: 150px; left: 70%; width: 100px; height: 100px; animation-delay: 3s;}
    @keyframes floatAnim {0% {transform: translateY(0);}50% {transform: translateY(-15px);}100% {transform: translateY(0);}}

    .aes-card {
        background: rgba(255,255,255,0.03);
        backdrop-filter: blur(16px);
        border-radius: 25px;
        padding: 25px;
        margin-bottom: 30px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.25);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        position: relative;
    }
    .aes-card:hover {transform: translateY(-8px); box-shadow: 0 14px 32px rgba(0,0,0,0.35);}
    .aes-title {color: #a8c0ff; font-size: 24px; font-weight: 700; margin-bottom: 15px;}
    .aes-output {
        background: rgba(255,255,255,0.05);
        padding: 12px; border-radius: 15px;
        font-family: monospace; color: #fff;
        margin-top: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        word-break: break-all;
    }
    .aes-btn {
        background: linear-gradient(90deg, #627daa, #a8c0ff);
        border: none;
        color: white;
        font-weight: 600;
        padding: 12px 28px;
        border-radius: 15px;
        cursor: pointer;
        transition: all 0.3s ease;
        margin-top: 12px;
        font-size: 16px;
    }
    .aes-btn:hover {
        background: linear-gradient(90deg, #a8c0ff, #fbc2eb);
        transform: scale(1.08);
        box-shadow: 0 8px 24px rgba(168,192,255,0.4);
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- Floating Circles ----------
    st.markdown("""
    <div class="float-circle"></div>
    <div class="float-circle"></div>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color:#a8c0ff; font-weight:700; margin-bottom:10px;">Row Transposition Cipher</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#cfd8ff">Implementation uses your `row_transposition` and `row_transposition_decrypt` functions. Key must be numeric digits (e.g. 4312567).</p>', unsafe_allow_html=True)

    # ---------- Encryption Card ----------
    st.markdown('<div class="aes-card">', unsafe_allow_html=True)
    st.markdown('<div class="aes-title">Encryption</div>', unsafe_allow_html=True)
    plaintext = st.text_area("Plaintext (spaces will be removed, result uppercased)", key="plain_input", height=120)
    key_enc = st.text_input("Key (digits only, e.g. 4312567)", key="key_enc")
    if st.button("Encrypt", key="btn_enc"):
        try:
            if not key_enc or not key_enc.isdigit() or len(key_enc) < 2:
                st.error("Key must be numeric (digits only) and at least 2 digits long.")
            else:
                cipher = row_transposition_encryption(plaintext, key_enc)
                st.markdown(f'<div class="aes-output">{cipher}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error: {e}")
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- Decryption Card ----------
    st.markdown('<div class="aes-card">', unsafe_allow_html=True)
    st.markdown('<div class="aes-title">Decryption</div>', unsafe_allow_html=True)
    cipher_input = st.text_area("Ciphertext (already uppercase, no spaces)", key="cipher_input", height=120)
    key_dec = st.text_input("Key (digits only, same key used for encryption)", key="key_dec")
    if st.button("Decrypt", key="btn_dec"):
        try:
            if not key_dec or not key_dec.isdigit() or len(key_dec) < 2:
                st.error("Key must be numeric (digits only) and at least 2 digits long.")
            else:
                # ensure ciphertext length is divisible by key length (it should be if encrypted by the same function)
                if len(cipher_input) % len(key_dec) != 0:
                    st.warning("Warning: ciphertext length is not a multiple of key length. Decrypt will proceed but result may be incorrect.")
                plaintext_out = row_transposition_decrypt(cipher_input, key_dec)
                st.markdown(f'<div class="aes-output">{plaintext_out}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error: {e}")
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    show_row_cipher_page()
