import streamlit as st
from Crypto.Cipher import AES
import base64

# ---------------- Helper Functions ----------------
BLOCK_SIZE = 16  # AES-128

def pad_bytes(data):
    pad_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([pad_len] * pad_len)

def unpad_bytes(data):
    pad_len = data[-1]
    return data[:-pad_len]

def aes_encrypt(text, key):
    if len(key) != 16:
        raise ValueError("Key must be exactly 16 characters!")
    key_bytes = key.encode("utf-8")
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    text_bytes = text.encode("utf-8")
    encrypted = cipher.encrypt(pad_bytes(text_bytes))
    return base64.b64encode(encrypted).decode("utf-8")

def aes_decrypt(enc, key):
    if len(key) != 16:
        raise ValueError("Key must be exactly 16 characters!")
    key_bytes = key.encode("utf-8")
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    enc_bytes = base64.b64decode(enc)
    decrypted = cipher.decrypt(enc_bytes)
    return unpad_bytes(decrypted).decode("utf-8")

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

# ---------------- AES Page ----------------
def show_aes_page():
    st.set_page_config(page_title="AES Cipher", layout="wide")
    st.markdown("<h1 style='text-align:center; color:#CF60CA;'>AES Encryption / Decryption</h1>", unsafe_allow_html=True)

    # ---------- Text Encryption / Decryption ----------
    st.markdown("<h3 style='color:#cc99ff;'>Text Encryption / Decryption</h3>", unsafe_allow_html=True)
    text_input = st.text_input("Plaintext / Cipher")
    key_input = st.text_input("Key (16 chars)")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Encrypt Text"):
            if not text_input or not key_input:
                st.warning("⚠️ Please enter both text and key.")
            else:
                try:
                    enc = aes_encrypt(text_input.strip(), key_input.strip())
                    add_to_history("AES", "Encryption", text_input, enc)
                    st.success("✅ Text Encrypted Successfully!")
                    st.text_area("Encrypted Text Preview", enc, height=150)
                except Exception as e:
                    st.error(f"❌ {e}")
    with col2:
        if st.button("Decrypt Text"):
            if not text_input or not key_input:
                st.warning("⚠️ Please enter both cipher text and key.")
            else:
                try:
                    dec = aes_decrypt(text_input.strip(), key_input.strip())
                    add_to_history("AES", "Decryption", text_input, dec)
                    st.success("✅ Text Decrypted Successfully!")
                    st.text_area("Decrypted Text Preview", dec, height=150)
                except Exception as e:
                    st.error(f"❌ {e}")

    # ---------- File Encryption / Decryption ----------
    st.markdown("<h3 style='color:#cc99ff;'>File Encryption / Decryption</h3>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
    file_key = st.text_input("File Key (16 chars)", key="aes_file_key_tab2")

    if uploaded_file and file_key:
        file_content = uploaded_file.read().decode("utf-8")
        col3, col4 = st.columns([1,1])
        with col3:
            if st.button("Encrypt File"):
                try:
                    cipher_file = aes_encrypt(file_content, file_key.strip())
                    add_to_history("AES", "Encryption", file_content, cipher_file)
                    st.success("✅ File Encrypted Successfully!")
                    st.download_button(
                        label="⬇ Download Encrypted File",
                        data=cipher_file,
                        file_name=f"{uploaded_file.name.replace('.txt','')}_encrypted.txt",
                        mime="text/plain"
                    )
                    st.text_area("Encrypted File Preview", cipher_file, height=150)
                except Exception as e:
                    st.error(f"❌ {e}")
        with col4:
            if st.button("Decrypt File"):
                try:
                    plain_file = aes_decrypt(file_content, file_key.strip())
                    add_to_history("AES", "Decryption", file_content, plain_file)
                    st.success("✅ File Decrypted Successfully!")
                    st.download_button(
                        label="⬇ Download Decrypted File",
                        data=plain_file,
                        file_name=f"{uploaded_file.name.replace('.txt','')}_decrypted.txt",
                        mime="text/plain"
                    )
                    st.text_area("Decrypted File Preview", plain_file, height=150)
                except Exception as e:
                    st.error(f"❌ {e}")

# =========================
# Show AES page directly
# =========================
show_aes_page()
