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
    st.markdown('<h1 style="text-align:center; color:#CF60CA; font-weight:700; margin-bottom:25px;">DNA Encryption / Decryption</h1>', unsafe_allow_html=True)
    
    # Initialize state
    for key in ["plain_text", "cipher_text", "result_encrypt", "result_decrypt"]:
        if key not in st.session_state:
            st.session_state[key] = ""

    # ============= TEXT ENC/DEC =============
    st.markdown("<h3 style='color:#cc99ff;'> TEXT Encryption / Decryption</h3>", unsafe_allow_html=True)

    text_input = st.text_input("Plaintext / Cipher (DNA)")
    key_input = st.text_input("Key")

    result_e = ""
    result_d = ""

    col1, col2 = st.columns(2)

    # Encrypt
    with col1:
        if st.button("Encrypt Text"):
            if not text_input or not key_input:
                st.warning("⚠️ Please enter both text and key.")
            else:
                result_e = dna_encrypt(text_input.strip(), key_input.strip())
                st.session_state.result_encrypt = result_e
                add_to_history("DNA", "Encryption", text_input, result_e)

    # Decrypt
    with col2:
        if st.button("Decrypt Text"):
            if not text_input or not key_input:
                st.warning("⚠️ Please enter both cipher and key.")
            else:
                try:
                    result_d = dna_decrypt(text_input.strip(), key_input.strip())
                    st.session_state.result_decrypt = result_d
                    add_to_history("DNA", "Decryption", text_input, result_d)
                except:
                    st.error("❌ Failed to decrypt! Check key or cipher.")

    # Show results
    if st.session_state.result_encrypt:
        st.subheader("Encryption")
        st.code(st.session_state.result_encrypt)

    if st.session_state.result_decrypt:
        st.subheader("Decryption")
        st.code(st.session_state.result_decrypt)

    # ============= FILE ENC/DEC =============
    st.markdown("<h3 style='color:#cc99ff;'> File Encryption / Decryption</h3>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
    file_key = st.text_input("File Key", key="file_key_tab_DNA")

    if uploaded_file and file_key:
        file_content = uploaded_file.read().decode("utf-8")

        col3, col4 = st.columns([1,1])

        # Encrypt File
        with col3:
            if st.button("Encrypt File"):
                cipher_file = dna_encrypt(file_content, file_key)
                add_to_history("DNA", "Encryption", file_content, cipher_file)
                st.success("✅ File Encrypted Successfully!")

                st.download_button(
                    "⬇ Download Encrypted File",
                    cipher_file,
                    file_name=f"{uploaded_file.name.replace('.txt','')}_encrypted.txt",
                    mime="text/plain"
                )
                st.text_area("Encrypted File Preview", cipher_file, height=150)

        # Decrypt File
        with col4:
            if st.button("Decrypt File"):
                try:
                    plain_file = dna_decrypt(file_content, file_key)
                    add_to_history("DNA", "Decryption", file_content, plain_file)
                    st.success("✅ File Decrypted Successfully!")

                    st.download_button(
                        "⬇ Download Decrypted File",
                        plain_file,
                        file_name=f"{uploaded_file.name.replace('.txt','')}_decrypted.txt",
                        mime="text/plain"
                    )
                    st.text_area("Decrypted File Preview", plain_file, height=150)
                except:
                    st.error("❌ Failed to decrypt file!")


# Run directly
show_dna_page()
