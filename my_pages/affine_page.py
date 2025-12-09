# my_pages/affine_page.py
import streamlit as st
from algorithms.affine import affine_encrypt, affine_decrypt

# ---------------- History Helper ----------------
def add_to_history(algo, action, input_text, output_text):
    if "history" not in st.session_state:
        st.session_state["history"] = []
    st.session_state["history"].append({
        "algo": algo,
        "action": action,
        "input": input_text,
        "output": output_text
    })

# ---------------- Affine Page UI ----------------
def show_affine_page():
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

    .affine-card {
        background: rgba(255,255,255,0.03);
        backdrop-filter: blur(16px);
        border-radius: 25px;
        padding: 25px;
        margin-bottom: 30px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.25);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        position: relative;
    }
    .affine-card:hover {transform: translateY(-8px); box-shadow: 0 14px 32px rgba(0,0,0,0.35);}
    .affine-title {color: #a8c0ff; font-size: 24px; font-weight: 700; margin-bottom: 15px;}
    .affine-output {
        background: rgba(255,255,255,0.05);
        padding: 12px; border-radius: 15px;
        font-family: monospace; color: #fff;
        margin-top: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        word-break: break-all;
    }
    .affine-btn {
        background: linear-gradient(90deg, #627daa, #a8c0ff);
        border: none;
        color: white;
        font-weight: 600;
        padding: 16px 32px;
        border-radius: 20px;
        cursor: pointer;
        transition: all 0.3s ease;
        margin-top: 20px;
        font-size: 18px;
        width: 100%;
    }
    .affine-btn:hover {
        background: linear-gradient(90deg, #a8c0ff, #fbc2eb);
        transform: scale(1.05);
        box-shadow: 0 8px 24px rgba(168,192,255,0.4);
    }
    div.stTextInput>div>input {
        background: rgba(255,255,255,0.05) !important;
        color: #ffffff !important;
        border-radius: 15px;
        padding: 10px;
        border: 1px solid rgba(255,255,255,0.2);
        font-size: 16px;
    }
    div.stTextInput>div>input::placeholder {
        color: #b0b0b0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- Floating Circles ----------
    st.markdown("""
    <div class="float-circle"></div>
    <div class="float-circle"></div>
    """, unsafe_allow_html=True)
 #st.title("Affine Encryption / Decryption")
    st.markdown('<h1 style="text-align:center; color:#CF60CA; font-weight:700; margin-bottom:25px;">Affine Encrypyion/ Decryption </h1>', unsafe_allow_html=True)
    st.markdown("<h3 style='color:#cc99ff;'> TEXT Encryption / Decryption</h3>", unsafe_allow_html=True)
    # ---------- Input fields ----------
    txt = st.text_input("Text", key="affine_text")
    a = st.number_input("Key a", min_value=1, max_value=25, step=1, key="affine_a")
    b = st.number_input("Key b", min_value=0, max_value=25, step=1, key="affine_b")

    # ---------- Buttons in same row ----------
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Encrypt", key="affine_enc_btn"):
            try:
                enc_text = affine_encrypt(txt, a, b)
                if enc_text:
                   st.subheader("Decryption")
                   st.code( enc_text)
                add_to_history("Affine", "Encryption", txt, enc_text)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    with col2:
        if st.button("Decrypt", key="affine_dec_btn"):
            try:
                dec_text = affine_decrypt(txt, a, b)
                if dec_text:
                   st.subheader("Decryption")
                   st.code( dec_text)
              
                add_to_history("Affine", "Decryption", txt, dec_text)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    st.markdown("<h3 style='color:#cc99ff;'> File Encryption / Decryption</h3>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"], key="affine")
    afile = st.number_input("Key a", min_value=1, max_value=25, step=1, key="affine_afile")
    bfile = st.number_input("Key b", min_value=0, max_value=25, step=1, key="affine_bfile")
    if uploaded_file and afile and bfile :
              file_content = uploaded_file.read().decode("utf-8")
              col3, col4 = st.columns([1,1])
              with col3:
                if st.button("Encrypt File"):
                    cipher_file = affine_encrypt(file_content, afile,bfile)
                    add_to_history("DES", "Encryption", file_content, cipher_file)
                    st.success("✅ File Encrypted Successfully!")
                    st.download_button(
                        label="⬇ Download Encrypted File",
                        data=cipher_file,
                        file_name=f"{uploaded_file.name.replace('.txt','')}_encrypted.txt",
                        mime="text/plain"
                    )
                    st.text_area("Encrypted File Preview", cipher_file, height=150)
              with col4:
                if st.button("Decrypt File"):
                    try:
                        plain_file = affine_decrypt(file_content, afile,bfile)
                        add_to_history("DES", "Decryption", file_content, plain_file)
                        st.success("✅ File Decrypted Successfully!")
                        st.download_button(
                            label="⬇ Download Decrypted File",
                            data=plain_file,
                            file_name=f"{uploaded_file.name.replace('.txt','')}_decrypted.txt",
                            mime="text/plain"
                        )
                        st.text_area("Decrypted File Preview", plain_file, height=150)
                    except Exception as e:
                        st.error(f"❌ Failed to decrypt: {e}")
               



