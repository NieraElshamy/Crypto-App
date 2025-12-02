import streamlit as st
from my_pages.affine_page import show_affine_page
from my_pages.dna_page import show_dna_page
from my_pages.vigenere_page import show_vigenere_page
from my_pages.row_page import show_row_page
from my_pages.des_page import show_des_page
from my_pages.aes_page import show_aes_page
from my_pages.history_page import show_history_page

st.set_page_config(page_title="Crypto App", layout="wide")

with st.sidebar:
    st.markdown("<h1>Crypto App</h1>", unsafe_allow_html=True)
    page = st.radio(
        "Navigate to:",
        ["Dashboard", "Affine", "DNA", "Vigenère", "Row Transposition", "DES", "AES", "History"],
        key="menu"
    )

# ---------------------- Pages ----------------------
if page == "Dashboard":
    st.title("Welcome to Crypto App")
    st.write("Choose an algorithm from the sidebar to begin.")

elif page == "Affine":
    st.title("Affine Cipher")
    show_affine_page()

elif page == "DNA":
    st.title("DNA Encryption")
    show_dna_page()

elif page == "Vigenère":
    st.title("Vigenère Cipher")
    show_vigenere_page()

elif page == "Row Transposition":
    st.title("Row Transposition Cipher")
    show_row_page()

elif page == "DES":
    st.title("DES Encryption")
    show_des_page()

elif page == "AES":
    st.title("AES Encryption")
    show_aes_page()

elif page == "History":
    st.title("History")
    show_history_page()

# Add custom CSS to make buttons look like the design
st.markdown("""
<style>
/* Style for main category buttons (SIDE BY SIDE) */
div[data-testid="column"] button {
    background: linear-gradient(145deg, rgba(50,55,75,0.95), rgba(35,40,60,0.95)) !important;
    border: 2px solid rgba(168,192,255,0.15) !important;
    border-radius: 20px !important;
    padding: 25px 20px !important;
    color: #a8c0ff !important;
    font-size: 26px !important;
    font-weight: 700 !important;
    text-align: center !important;
    height: 180px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    flex-direction: column !important;
    transition: all 0.3s ease !important;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.15) !important;
    white-space: normal !important;
    word-wrap: break-word !important;
    overflow-wrap: break-word !important;
    line-height: 1.4 !important;
}

div[data-testid="column"] button:hover {
    transform: translateY(-5px) !important;
    box-shadow: 0px 15px 35px rgba(0,0,0,0.25) !important;
    border: 2px solid rgba(168,192,255,0.3) !important;
}

/* Add gradient border on hover */
div[data-testid="column"] button:hover::before {
    content: '';
    position: absolute;
    top: -2px;
    left: -2px;
    right: -2px;
    bottom: -2px;
    background: linear-gradient(90deg, #a8c0ff, #fbc2eb);
    border-radius: 22px;
    z-index: -1;
    animation: borderGlow 2s infinite alternate;
}

@keyframes borderGlow {
    from { opacity: 0.5; }
    to { opacity: 1; }
}

/* Style for small flashcard buttons */
div[data-testid="stButton"] button {
    background: linear-gradient(145deg, rgba(40,45,65,0.9), rgba(25,30,45,0.9)) !important;
    border: 1px solid rgba(168,192,255,0.1) !important;
    border-radius: 18px !important;
    padding: 25px 20px !important;
    color: #a8c0ff !important;
    text-align: center !important;
    height: auto !important;
    min-height: 160px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.12) !important;
    font-size: 22px !important;
    font-weight: 600 !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    align-items: center !important;
}

div[data-testid="stButton"] button:hover {
    transform: translateY(-5px) !important;
    box-shadow: 0px 12px 30px rgba(0,0,0,0.2) !important;
    border: 1px solid rgba(168,192,255,0.2) !important;
}

/* Make sure all buttons have consistent styling */
button {
    border: none !important;
    outline: none !important;
}

/* Ensure columns have equal height */
div[data-testid="column"] {
    display: flex;
    flex-direction: column;
}

div[data-testid="column"] > div {
    flex: 1;
    display: flex;
}

div[data-testid="column"] button {
    flex: 1;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)