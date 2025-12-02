import streamlit as st

def format_text(s):
    return ''.join([c.upper() for c in s if c.isalpha()])

def vigenere_encrypt(p, key):
    p = format_text(p)
    key = format_text(key)
    res = ""
    for i, ch in enumerate(p):
        shift = ord(key[i % len(key)]) - 65
        res += chr((ord(ch) - 65 + shift) % 26 + 65)
    return res

def vigenere_decrypt(c, key):
    c = format_text(c)
    key = format_text(key)
    res = ""
    for i, ch in enumerate(c):
        shift = ord(key[i % len(key)]) - 65
        res += chr((ord(ch) - 65 - shift) % 26 + 65)
    return res

def show_vigenere_page():
    st.markdown("""
    <style>
    /* ==== Background Floating Shapes ==== */
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
    .float-circle:nth-child(1){ top: 30px; left: 15%; width: 70px; height: 70px;}
    .float-circle:nth-child(2){ top: 120px; left: 75%; width: 90px; height: 90px; animation-delay: 3s;}
    @keyframes floatAnim {0% {transform: translateY(0);}50% {transform: translateY(-12px);}100% {transform: translateY(0);}}

    /* ==== Vigenere Cards ==== */
    .vig-card {
        background: rgba(255,255,255,0.03);
        backdrop-filter: blur(16px);
        border-radius: 25px;
        padding: 25px;
        margin-bottom: 30px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.25);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .vig-card:hover {transform: translateY(-8px); box-shadow: 0 14px 32px rgba(0,0,0,0.35);}
    .vig-title {color: #a8c0ff; font-size: 24px; font-weight: 700; margin-bottom: 15px;}
    .vig-output {
        background: rgba(255,255,255,0.05);
        padding: 12px; border-radius: 15px;
        font-family: monospace; color: #fff;
        margin-top: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        word-break: break-all;
    }

    /* ==== Buttons ==== */
    .vig-btn {
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
    .vig-btn:hover {
        background: linear-gradient(90deg, #a8c0ff, #fbc2eb);
        transform: scale(1.08);
        box-shadow: 0 8px 24px rgba(168,192,255,0.4);
    }
    </style>
    """, unsafe_allow_html=True)

    # Floating Circles
    st.markdown("""
    <div class="float-circle"></div>
    <div class="float-circle"></div>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color:#a8c0ff; font-weight:700; margin-bottom:25px;">Vigenère Cipher</h1>', unsafe_allow_html=True)

    # Encryption Card
    st.markdown('<div class="vig-card">', unsafe_allow_html=True)
    st.markdown('<div class="vig-title">Encryption</div>', unsafe_allow_html=True)
    text = st.text_input("Plaintext", key="vig_plain")
    key = st.text_input("Key", key="vig_key1")
    if st.button("Encrypt", key="vig_enc_btn"):
        try:
            enc_text = vigenere_encrypt(text, key)
            st.markdown(f'<div class="vig-output">{enc_text}</div>', unsafe_allow_html=True)
        except:
            st.error("Error: Check your key and plaintext")
    st.markdown('</div>', unsafe_allow_html=True)

    # Decryption Card
    st.markdown('<div class="vig-card">', unsafe_allow_html=True)
    st.markdown('<div class="vig-title">Decryption</div>', unsafe_allow_html=True)
    text2 = st.text_input("Ciphertext", key="vig_cipher")
    key2 = st.text_input("Key", key="vig_key2")
    if st.button("Decrypt", key="vig_dec_btn"):
        try:
            dec_text = vigenere_decrypt(text2, key2)
            st.markdown(f'<div class="vig-output">{dec_text}</div>', unsafe_allow_html=True)
        except:
            st.error("Error: Check your key and ciphertext")
    st.markdown('</div>', unsafe_allow_html=True)
