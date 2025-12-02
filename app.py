import streamlit as st
from my_pages.affine_page import show_affine_page
from my_pages.dna_page import show_dna_page
from my_pages.vigenere_page import show_vigenere_page
from my_pages.row_page import show_row_page
from my_pages.des_page import show_des_page
from my_pages.aes_page import show_aes_page
from my_pages.history_page import show_history_page

st.set_page_config(page_title="Crypto App", layout="wide")

# ---------------------- Custom Dark Soft CSS ----------------------
st.markdown("""
<style>
/* ===== Body & Font ===== */
body, input, textarea {
    font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #0b0c10, #1c1f2a);
    background-size: 400% 400%;
    animation: bgAnim 20s ease infinite;
    color: #e0e0e0;
}

/* ===== Background Animation ===== */
@keyframes bgAnim {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* ===== Sidebar Styling ===== */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #11121b, #1f2330);
    padding-top: 35px;
    color: #e0e0e0;
    border-radius: 20px 0 0 20px;
}
[data-testid="stSidebar"] h1 {
    font-size: 24px;
    font-weight: 600;
    color: #dcdcdc;
    text-align: center;
    margin-bottom: 25px;
}
div.row-widget.stRadio > div {
    background: #1c1f2f;
    padding: 12px;
    border-radius: 12px;
    color: #ccc;
    transition: all 0.3s ease;
}
div.row-widget.stRadio > div:hover {
    background: #334466;
    color: #fff;
}

/* ===== Hero Section ===== */
.hero {
    width: 100%;
    height: 220px;
    background: linear-gradient(135deg, rgba(30,32,42,0.95), rgba(50,55,70,0.95));
    border-radius: 20px;
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.15);
    margin-bottom: 30px;
    animation: fadeIn 1.5s ease;
}
.hero h1 {
    color: #a8c0ff;
    font-size: 36px;
    font-weight: 700;
}

/* Floating Circles */
.circle {
    position: absolute;
    width: 70px;
    height: 70px;
    border-radius: 50%;
    background: rgba(168,192,255,0.08);
    animation: float 8s ease-in-out infinite;
}
.circle:nth-child(1){ top: 20px; left: 10%; animation-delay: 0s; }
.circle:nth-child(2){ top: 50px; left: 80%; animation-delay: 3s; }
@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-10px);}
    100% {transform: translateY(0px);}
}

/* ===== Cards ===== */
.cards {
    display: flex;
    gap: 25px;
    flex-wrap: wrap;
    justify-content: center;
}
.card {
    flex: 1 1 250px;
    min-height: 160px;
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0px 4px 16px rgba(0,0,0,0.12);
    transition: transform 0.4s ease, box-shadow 0.4s ease;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin-bottom: 20px;
    animation: popIn 0.8s ease;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 12px 24px rgba(0,0,0,0.2);
}
.card-title {
    font-size: 20px;
    font-weight: 600;
    color: #a8c0ff;
    margin-bottom: 10px;
}
.card-desc {
    font-size: 14px;
    color: #bbb;
    opacity: 0.85;
}
.bar {
    width: 60px;
    height: 5px;
    background: linear-gradient(90deg, #a8c0ff, #fbc2eb);
    border-radius: 6px;
    margin-top: 12px;
    animation: barAnim 5s infinite alternate ease-in-out;
}

/* ===== Animations ===== */
@keyframes fadeIn {0%{opacity:0; transform:translateY(15px);}100%{opacity:1; transform:translateY(0);}}
@keyframes popIn {0%{transform:scale(0.95); opacity:0;}100%{transform:scale(1); opacity:1;}}
@keyframes barAnim {0%{width:30%;}100%{width:100%;}}
</style>
""", unsafe_allow_html=True)

# ---------------------- Sidebar ----------------------
with st.sidebar:
    st.markdown("<h1>Crypto App</h1>", unsafe_allow_html=True)
    page = st.radio(
        "Navigate to:",
        ["Dashboard", "Affine", "DNA", "Vigenère", "Row Transposition", "DES", "AES", "History"],
        key="menu"
    )

# ---------------------- Pages ----------------------
if page == "Dashboard":
    st.markdown("""
    <div class="hero">
        <h1>Welcome to Crypto App</h1>
        <div class="circle"></div>
        <div class="circle"></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="cards">
        <div class="card">
            <div class="card-title">Classical Ciphers</div>
            <div class="card-desc">Affine, Vigenère, DNA, and Row Transposition.</div>
            <div class="bar"></div>
        </div>
        <div class="card">
            <div class="card-title">Modern Encryption</div>
            <div class="card-desc">AES and DES block cipher systems.</div>
            <div class="bar"></div>
        </div>
        <div class="card">
            <div class="card-title">History Logs</div>
            <div class="card-desc">Track all operations performed in real-time.</div>
            <div class="bar"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

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
