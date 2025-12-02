import streamlit as st
from Crypto.Cipher import AES
import base64
##
# ---------------- Helper Functions ----------------
BLOCK_SIZE = 16  # AES-128

def pad_bytes(data):
    """Pad data to multiple of BLOCK_SIZE using PKCS7"""
    pad_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([pad_len] * pad_len)

def unpad_bytes(data):
    """Remove PKCS7 padding"""
    pad_len = data[-1]
    return data[:-pad_len]

def aes_encrypt(text, key):
    key_bytes = key.encode("utf-8")
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    text_bytes = text.encode("utf-8")
    encrypted = cipher.encrypt(pad_bytes(text_bytes))
    return base64.b64encode(encrypted).decode("utf-8")

def aes_decrypt(enc, key):
    key_bytes = key.encode("utf-8")
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    enc_bytes = base64.b64decode(enc)
    decrypted = cipher.decrypt(enc_bytes)
    return unpad_bytes(decrypted).decode("utf-8")

# ---------------- AES Page ----------------
def show_aes_page():
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

    st.markdown('<h1 style="color:#a8c0ff; font-weight:700; margin-bottom:25px;">AES Encryption / Decryption</h1>', unsafe_allow_html=True)

    # ---------- Encryption Card ----------
    st.markdown('<div class="aes-card">', unsafe_allow_html=True)
    st.markdown('<div class="aes-title">Encryption</div>', unsafe_allow_html=True)
    txt = st.text_input("Plaintext", key="aes_plain")
    key = st.text_input("Key (16 chars)", key="aes_key1")
    if st.button("Encrypt", key="aes_enc_btn"):
        try:
            if len(key) != 16:
                st.error("Key must be exactly 16 characters!")
            else:
                enc_text = aes_encrypt(txt, key)
                st.markdown(f'<div class="aes-output">{enc_text}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error: {str(e)}")
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------- Decryption Card ----------
    st.markdown('<div class="aes-card">', unsafe_allow_html=True)
    st.markdown('<div class="aes-title">Decryption</div>', unsafe_allow_html=True)
    txt2 = st.text_input("Ciphertext (Base64)", key="aes_cipher")
    key2 = st.text_input("Key", key="aes_key2")
    if st.button("Decrypt", key="aes_dec_btn"):
        try:
            if len(key2) != 16:
                st.error("Key must be exactly 16 characters!")
            else:
                dec_text = aes_decrypt(txt2, key2)
                st.markdown(f'<div class="aes-output">{dec_text}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error: {str(e)}")
    st.markdown('</div>', unsafe_allow_html=True)
