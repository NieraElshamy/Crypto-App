import streamlit as st

# ---------------- Row Transposition Encryption ---------------- #
def row_transposition_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.upper()

    key_list = [int(k) for k in str(key)]
    n_col = len(key_list)
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

    # ترتيب الأعمدة حسب المفتاح
    cipher = ""
    sorted_key = sorted(key_list)

    for num in sorted_key:
        col = key_list.index(num)
        for r in range(n_row):
            cipher += matrix[r][col]

    return cipher


# ---------------- Row Transposition Decryption ---------------- #
def row_transposition_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key_list = [int(k) for k in str(key)]
    n_col = len(key_list)
    n_row = len(ciphertext) // n_col

    matrix = [['' for _ in range(n_col)] for _ in range(n_row)]

    sorted_key = sorted(key_list)
    col_order = [key_list.index(num) for num in sorted_key]

    idx = 0
    for col_idx in col_order:
        for row in range(n_row):
            if idx < len(ciphertext):
                matrix[row][col_idx] = ciphertext[idx]
                idx += 1

    plaintext = ""
    for r in range(n_row):
        for c in range(n_col):
            plaintext += matrix[r][c]

    return plaintext

# ---------------- History Helper ---------------- #
def add_to_history(algo, action, input_text, output_text):
    if "history" not in st.session_state:
        st.session_state["history"] = []
    st.session_state["history"].append({
        "algo": algo,       # "Row Transposition"
        "action": action,   # "Encryption" أو "Decryption"
        "input": input_text,
        "output": output_text
    })

# ---------------- Streamlit Page ---------------- #
def show_row_page():
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

    .vig-card {
        background: rgba(255,255,255,0.03);
        backdrop-filter: blur(16px);
        border-radius: 25px;
        padding: 25px;
        margin-bottom: 30px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.25);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        position: relative;
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
    .vig-btn {
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
    .vig-btn:hover {
        background: linear-gradient(90deg, #a8c0ff, #fbc2eb);
        transform: scale(1.05);
        box-shadow: 0 8px 24px rgba(168,192,255,0.4);
    }

    /* Input fields */
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
    

    # ------- #)
    st.markdown('<h1 style="text-align:center; color:#CF60CA; font-weight:700; margin-bottom:25px;">Row Transposition Encrypyion/ Decryption </h1>', unsafe_allow_html=True)
    st.markdown("<h3 style='color:#cc99ff;'> TEXT Encryption / Decryption</h3>", unsafe_allow_html=True)
    txt = st.text_input("Text", key="vig_text", 
                       help="Enter text containing only letters (other characters will be ignored)")
    key = st.text_input("Key", key="vig_key", 
                       help="Enter key containing only letters")

    # ---------- Buttons ----------
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Encrypt", key="row_enc_btn", help="Click to encrypt text"):
            if  not key   or not key.isdigit() or len(key) < 2:
                st.error("Key must be numeric (digits only) and at least 2 digits long.")
            try:
                enc_text = row_transposition_encrypt(txt, key)
                if enc_text:
                   st.subheader("Decryption")
                   st.code( enc_text)
                add_to_history("Row Transposition", "Encryption", txt, enc_text)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    with col2:
        if st.button("Decrypt", key="row_dec_btn", help="Click to decrypt text"):
            try:
                dec_text = row_transposition_decrypt(txt, key)
                if dec_text:
                   st.subheader("Decryption")
                   st.code( dec_text)
                add_to_history("Row Transposition", "Decryption", txt, dec_text)
            except Exception as e:
                st.error(f"Error: {str(e)}")
      # ---------- File Encryption / Decryption ----------
    st.markdown("<h3 style='color:#cc99ff;'> File Encryption / Decryption</h3>", unsafe_allow_html=True)


    uploaded_file = st.file_uploader("Upload a text file", type=["txt"], key="row_upload")
    file_key = st.text_input("File Key", key="file_key_tab2")

    if uploaded_file and file_key:
        file_content = uploaded_file.read().decode("utf-8")
        col3, col4 = st.columns([1,1])
        if  not file_key   or not file_key.isdigit() or len(file_key) < 2:
                st.error("Key must be numeric (digits only) and at least 2 digits long.")
        with col3:
            if st.button("Encrypt File"):
                cipher_file = row_transposition_encrypt(file_content, file_key.strip())
                add_to_history("Row Transposition", "Encryption", file_content, cipher_file)
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
                    plain_file =  row_transposition_decrypt(file_content, file_key.strip())
                    add_to_history("Row Transposition", "Decryption", file_content, plain_file)
                    st.success("✅ File Decrypted Successfully!")
                    st.download_button(
                        label="⬇ Download Decrypted File",
                        data=plain_file,
                        file_name=f"{uploaded_file.name.replace('.txt','')}_decrypted.txt",
                        mime="text/plain"
                    )
                    st.text_area("Decrypted File Preview", plain_file, height=150)
                except Exception as e:
                    st.error(f" Failed to decrypt: {e}")

    # ---------- Information Section ----------
    st.markdown('</div>', unsafe_allow_html=True)
