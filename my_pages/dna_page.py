import streamlit as st

# =========================
# Functions for Text ↔ DNA (UTF-8)
# =========================

def text_to_bin(text: str) -> str:
    return ''.join(f"{byte:08b}" for byte in text.encode('utf-8'))

def bin_to_text(binary_str: str) -> str:
    bytes_list = [int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8)]
    return bytes(bytes_list).decode('utf-8', errors='ignore')

def xor_operation(text_bin: str, key_bin: str) -> str:
    return ''.join('0' if t_bit == key_bin[i % len(key_bin)] else '1' for i, t_bit in enumerate(text_bin))

def bin_to_dna(binary_str: str) -> str:
    dna_map = {"00": "A", "01": "T", "10": "C", "11": "G"}
    dna = ''
    for i in range(0, len(binary_str), 2):
        pair = binary_str[i:i+2].ljust(2, '0')
        dna += dna_map.get(pair, '')
    return dna

def dna_to_bin(dna: str) -> str:
    bin_map = {"A": "00", "T": "01", "C": "10", "G": "11"}
    return ''.join(bin_map.get(ch.upper(), '') for ch in dna)

def dna_encrypt(text: str, key: str) -> str:
    return bin_to_dna(xor_operation(text_to_bin(text), text_to_bin(key)))

def dna_decrypt(cipher: str, key: str) -> str:
    return bin_to_text(xor_operation(dna_to_bin(cipher), text_to_bin(key)))

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
# DNA Page
# =========================

def show_dna_page():
    st.set_page_config(page_title="🧬 DNA Cipher", layout="wide")
    st.markdown("<h1 style='text-align: center; color: #CF60CA;'>🧬 DNA Cipher Tool</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #cc99ff;'>Encrypt/Decrypt Texts & Files (UTF-8 Supported)</h4>", unsafe_allow_html=True)
    st.markdown("---")

    tabs = st.tabs(["💬 Text Encryption", "📄 File Encryption"])
    
    # ---------------- Text Tab ----------------
    with tabs[0]:
        st.markdown("<h3 style='color:#cc99ff;'>Text Encryption / Decryption</h3>", unsafe_allow_html=True)

        if "plain_text" not in st.session_state:
            st.session_state.plain_text = ""
        if "cipher_text" not in st.session_state:
            st.session_state.cipher_text = ""
        if "result_text" not in st.session_state:
            st.session_state.result_text = ""

        plain_text = st.text_area("Enter Plain Text", st.session_state.plain_text, height=120)
        cipher_text = st.text_area("Enter Cipher Text", st.session_state.cipher_text, height=120)
        key_text = st.text_input("Enter Key", type="default")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Encrypt Text", use_container_width=True):
                if plain_text and key_text:
                    result = dna_encrypt(plain_text, key_text)
                    st.session_state.result_texte = result
                    st.session_state.cipher_text = result
                    add_to_history("DNA", "Encryption", plain_text, result)
                    st.success("✅ Text Encrypted Successfully!")
                else:
                    st.error("⚠ Please enter text and key.")
        with col2:
            if st.button("Decrypt Text", use_container_width=True):
                if cipher_text and key_text:
                    try:
                        result = dna_decrypt(cipher_text, key_text)
                        st.session_state.result_textd = result
                        st.session_state.plain_text = result
                        add_to_history("DNA", "Decryption", cipher_text, result)
                        st.success("✅ Text Decrypted Successfully!")
                    except Exception as e:
                        st.error(f"❌ Failed to decrypt: {e}")
                else:
                    st.error("⚠ Please enter cipher text and key.")
        if st.session_state.result_texte:
            #st.text_area("Result Preview", st.session_state.result_text, height=100)
            st.subheader("Encryption")
            st.code(st.session_state.result_texte)
        if st.session_state.result_textd:
            #st.text_area("Result Preview", st.session_state.result_text, height=100)
            st.subheader("Decryption")
            st.code(st.session_state.result_textd)
    # ---------------- File Tab ----------------
    with tabs[1]:
        st.markdown("<h3 style='color:#cc99ff;'>File Encryption / Decryption</h3>", unsafe_allow_html=True)

        uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
        file_key = st.text_input("File Key", key="file_key_tab2")

        if uploaded_file and file_key:
            file_content = uploaded_file.read().decode("utf-8")
            col3, col4 = st.columns([1,1])
            with col3:
                if st.button("Encrypt File"):
                    cipher_file = dna_encrypt(file_content, file_key)
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
                        plain_file = dna_decrypt(file_content, file_key)
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

# =========================
# Show DNA page directly
# =========================


