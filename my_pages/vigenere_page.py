import streamlit as st
from algorithms.vigenere_cipher import vigenere_encrypt, vigenere_decrypt

# =========================
# History Helper
# =========================
def add_to_history(algo, action, input_text, output_text):
    if "history" not in st.session_state:
        st.session_state["history"] = []
    st.session_state["history"].append({
        "algo": algo,
        "action": action,
        "input": input_text,
        "output": output_text
    })

# =========================
# Vigenère Page
# =========================
def show_vigenere_page():
    #st.title("Vigenère Encryption / Decryption")
    #st.set_page_config(page_title=" Vigenère Cipher", layout="wide")
    st.markdown("<h1 style='text-align:center; color:#CF60CA;'>Vigenère Cipher Tool</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center; color:#cc99ff;'>Encrypt/Decrypt Texts & Files</h4>", unsafe_allow_html=True)
    st.markdown("---")
    
    # ---------- Text Encryption / Decryption ----------
    st.markdown("<h3 style='color:#cc99ff;'> Text Encryption / Decryption</h3>", unsafe_allow_html=True)
    text_input = st.text_input("Plaintext / Cipher")
    key_input = st.text_input("Key")

    result_e = ""
    result_d = ""

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Encrypt"):
            if not text_input or not key_input:
                st.warning("⚠️ Please enter both text and key.")
            else:
                result_e = vigenere_encrypt(text_input.strip(), key_input.strip())
                add_to_history("Vigenère", "Encryption", text_input, result_e)
    with col2:
        if st.button("Decrypt"):
            if not text_input or not key_input:
                st.warning("⚠️ Please enter both text and key.")
            else:
                result_d = vigenere_decrypt(text_input.strip(), key_input.strip())
                add_to_history("Vigenère", "Decryption", text_input, result_d)

    if result_e:
        st.subheader("Encryption")
        st.code(result_e)
    if result_d:
        st.subheader("Decryption")
        st.code(result_d)

    # ---------- File Encryption / Decryption ----------
    st.markdown("<h3 style='color:#cc99ff;'> File Encryption / Decryption</h3>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload a text file", type=["txt"], key="vigenere_upload")
    file_key = st.text_input("File Key", key="file_key_tab2")

    if uploaded_file and file_key:
        file_content = uploaded_file.read().decode("utf-8")
        col3, col4 = st.columns([1,1])
        with col3:
            if st.button("Encrypt File"):
                cipher_file = vigenere_encrypt(file_content, file_key.strip())
                add_to_history("Vigenère", "Encryption", file_content, cipher_file)
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
                    plain_file = vigenere_decrypt(file_content, file_key.strip())
                    add_to_history("Vigenère", "Decryption", file_content, plain_file)
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

# =========================
# Show Vigenère page
# =========================

