import streamlit as st
from pyDes import des, ECB, PAD_PKCS5
###from pyDes import des, ECB, PAD_PKCS5

# دالة التشفير
def des_encryptt(plaintext, key):
  
    if len(key.encode('utf-8')) != 8:
        return "❌ Key must be exactly 8 characters"
    cipher = des(key.encode('utf-8'), ECB, padmode=PAD_PKCS5)
    encrypted = cipher.encrypt(plaintext.encode('utf-8'))  # تحويل النص لبايتس
    return encrypted.hex()  # رجعنا النص المتشفر بالهيكسا

# دالة فك التشفير
def des_decryptt(ciphertext_hex, key):
    if len(key.encode('utf-8')) != 8:
        return "❌ Key must be exactly 8 characters"
    try:
        cipher_bytes = bytes.fromhex(ciphertext_hex.strip())
    except :
        return "❌ Input must be HEX"

    try:
     cipher = des(key.encode('utf-8'), ECB, padmode=PAD_PKCS5)
     encrypted_bytes = bytes.fromhex(ciphertext_hex)
     decrypted = cipher.decrypt(encrypted_bytes)
     return decrypted.decode('utf-8') 
    except Exception:
        return "❌ Failed: Decryption error (check key or ciphertext)"
   # النص الأصلي يرجع


def add_to_history(algo, action, input_text, output_text):
    if "history" not in st.session_state:
        st.session_state["history"] = []
    st.session_state["history"].append({
        "algo": algo,       # "Vigenère"
        "action": action,   # "Encryption" أو "Decryption"
        "input": input_text,
        "output": output_text
    })

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
    #st.title("DES Encryption / Decryption")
    st.markdown('<h1 style="text-align:center; color:#CF60CA; font-weight:700; margin-bottom:25px;">DES Encrypyion/ Decryption </h1>', unsafe_allow_html=True)
    st.markdown("<h3 style='color:#cc99ff;'> TEXT Encryption / Decryption</h3>", unsafe_allow_html=True)
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
                result_e = des_encryptt(text_input.strip(), key_input.strip())
                add_to_history("DES", "Encryption", text_input, result_e)
    with col2:
        if st.button("Decrypt"):
            if not text_input or not key_input:
                st.warning("⚠️ Please enter both text and key.")
            else:
                result_d = des_decryptt(text_input.strip(), key_input.strip())
                add_to_history("DES", "Decryption", text_input, result_d)
    if result_e:
      st.subheader("Encryption")
      st.code(result_e)
    if result_d:
      st.subheader("Decryption")
      st.code(result_d)
    #st.markdown('<h1 style="text-align:center; color:#600080; font-weight:700; margin-bottom:25px;"> FILE Encryption / Decryption</h1>', unsafe_allow_html=True)
    st.markdown("<h3 style='color:#cc99ff;'> File Encryption / Decryption</h3>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
    file_key = st.text_input("File Key", key="file_key_tab2")

    if uploaded_file and file_key:
            if len(file_key) != 8:
                 st.text_area("Error", "❌ Key must be exactly 8 characters", height=20)
            else:
              file_content = uploaded_file.read().decode("utf-8")
              col3, col4 = st.columns([1,1])
              with col3:
                if st.button("Encrypt File"):
                    cipher_file = des_encryptt(file_content, file_key)
                    add_to_history("DNA", "Encryption", file_content, cipher_file)
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
                        plain_file = des_decryptt(file_content, file_key)
                        add_to_history("DNA", "Decryption", file_content, plain_file)
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

