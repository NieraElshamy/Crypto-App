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

/* ===== Main Category Cards Container (SIDE BY SIDE) ===== */
.main-cards-row {
    display: flex;
    gap: 25px;
    justify-content: center;
    margin: 20px 0 40px 0;
    width: 100%;
}

/* ===== Main Category Cards (Large Cards - SIDE BY SIDE) ===== */
.main-category-card {
    flex: 1;
    min-width: 4000px;
    max-width: 500px;
    height: 180px;
    background: linear-gradient(145deg, rgba(50,55,75,0.95), rgba(35,40,60,0.95));
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.15);
    transition: all 0.4s ease;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    border: 2px solid rgba(168,192,255,0.15);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}

.main-category-card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 15px 35px rgba(0,0,0,0.25);
    border: 2px solid rgba(168,192,255,0.3);
}

.main-category-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #a8c0ff, #fbc2eb);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.main-category-card:hover::before {
    opacity: 1;
}

.main-card-title {
    font-size: 60px;
    font-weight: 900;
    color: #a8c0ff;
    margin-bottom: 10px;
}

.main-card-desc {
    font-size: 40px;
    color: #bbb;
    line-height: 1.5;
    opacity: 0.9;
}

/* ===== Small Flash Cards Container ===== */
.small-cards-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 25px;
    margin: 30px 0 40px 0;
}

/* ===== Small Flash Cards ===== */
.small-flashcard {
    background: linear-gradient(145deg, rgba(40,45,65,0.9), rgba(25,30,45,0.9));
    border-radius: 18px;
    padding: 25px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.12);
    transition: all 0.3s ease;
    cursor: pointer;
    border: 1px solid rgba(168,192,255,0.1);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    min-height: 160px;
}

.small-flashcard:hover {
    transform: translateY(-5px);
    box-shadow: 0px 12px 30px rgba(0,0,0,0.2);
    border: 1px solid rgba(168,192,255,0.2);
}

.small-card-title {
    font-size: 22px;
    font-weight: 600;
    color: #a8c0ff;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.small-card-desc {
    font-size: 15px;
    color: #aaa;
    line-height: 1.5;
    opacity: 0.9;
}

/* ===== History Card ===== */
.history-card {
    width: 100%;
    max-width: 650px;
    margin: 40px auto;
    background: linear-gradient(145deg, rgba(45,50,70,0.95), rgba(30,35,50,0.95));
    border-radius: 18px;
    padding: 25px;
    box-shadow: 0px 8px 22px rgba(0,0,0,0.15);
    transition: all 0.3s ease;
    cursor: pointer;
    border: 1px solid rgba(168,192,255,0.12);
    text-align: center;
}

.history-card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 15px 30px rgba(0,0,0,0.2);
    border: 1px solid rgba(168,192,255,0.25);
}

.history-card-title {
    font-size: 24px;
    font-weight: 700;
    color: #a8c0ff;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
}

.history-card-desc {
    font-size: 16px;
    color: #bbb;
    line-height: 1.5;
}

/* ===== Section Headers ===== */
.section-header {
    color: #a8c0ff;
    font-size: 26px;
    font-weight: 700;
    margin: 40px 0 25px 0;
    text-align: center;
}

/* ===== Responsive Design ===== */
@media (max-width: 900px) {
    .main-cards-row {
        flex-direction: column;
        align-items: center;
    }
    .main-category-card {
        width: 100%;
        max-width: 100%;
    }
    .small-cards-container {
        grid-template-columns: 1fr;
    }
}

/* ===== Animations ===== */
@keyframes fadeIn {0%{opacity:0; transform:translateY(15px);}100%{opacity:1; transform:translateY(0);}}
@keyframes popIn {0%{transform:scale(0.95); opacity:0;}100%{transform:scale(1); opacity:1;}}
@keyframes float {0%{transform:translateY(0px);}50%{transform:translateY(-10px);}100%{transform:translateY(0px);}}
</style>
""", unsafe_allow_html=True)

# ---------------------- Flashcard Data ----------------------
FLASHCARDS_DATA = {
    "main_categories": [
        {
            "title": "Classical Ciphers",
            "description": "",
            "type": "main_category",
            "color": "#4a86e8"
        },
        {
            "title": "Modern Encryption",
            "description": "",
            "type": "main_category",
            "color": "#6aa84f"
        }
    ],
    "classical_ciphers": [
        {
            "title": "Affine Cipher",
            "description": "A monoalphabetic substitution cipher using mathematical functions.",
            "page": "Affine",
            "icon": ""
        },
        {
            "title": "Vigenère Cipher",
            "description": "A polyalphabetic substitution cipher using a keyword.",
            "page": "Vigenère",
            "icon": ""
        },
        {
            "title": "DNA Encryption",
            "description": "Encryption based on DNA sequences and biological concepts.",
            "page": "DNA",
            "icon": ""
        },
        {
            "title": "Row Transposition",
            "description": "A transposition cipher that rearranges characters in rows.",
            "page": "Row Transposition",
            "icon": ""
        }
    ],
    "modern_encryption": [
        {
            "title": "DES Encryption",
            "description": "Data Encryption Standard - A symmetric-key block cipher.",
            "page": "DES",
            "icon": ""
        },
        {
            "title": "AES Encryption",
            "description": "Advanced Encryption Standard - The most widely used encryption.",
            "page": "AES",
            "icon": ""
        }
    ],
    "history": [
        {
            "title": "History",
            "description": "Learn about the evolution of cryptography through time.",
            "page": "History",
            "icon": ""
        }
    ]
}
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
    # Hero Section
    st.markdown("""
    <div class="hero">
        <h1>Welcome to Crypto App</h1>
        <div class="circle"></div>
        <div class="circle"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Title
    st.markdown("<h2 style='text-align: center; color: #a8c0ff; margin-bottom: 20px;'>Explore Cryptography</h2>", unsafe_allow_html=True)
    
    # --- DISPLAY MAIN CATEGORY CARDS SIDE BY SIDE ---
    st.markdown("<div class='main-cards-row'>", unsafe_allow_html=True)
    
    # إنشاء عمودين لجعل البطاقتين جنب بعض
    col1, col2 = st.columns(2)
    
    # Classical Ciphers Card
    with col1:
        classical_card = FLASHCARDS_DATA["main_categories"][0]
        if st.button(
            f"### {classical_card['title']}\n\n{classical_card['description']}",
            use_container_width=True,
            key="main_classical"
        ):
            st.session_state.scroll_to = "classical"
    
    # Modern Encryption Card
    with col2:
        modern_card = FLASHCARDS_DATA["main_categories"][1]
        if st.button(
            f"### {modern_card['title']}\n\n{modern_card['description']}",
            use_container_width=True,
            key="main_modern"
        ):
            st.session_state.scroll_to = "modern"
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # --- Classical Ciphers Section ---
    st.markdown("<div class='section-header'>Classical Ciphers</div>", unsafe_allow_html=True)
    
    # إنشاء فلاش كارد صغيرة لل Classical Ciphers
    classical_cols = st.columns(2)
    for idx, card in enumerate(FLASHCARDS_DATA["classical_ciphers"]):
        col_idx = idx % 2
        with classical_cols[col_idx]:
            if st.button(
                f"#### {card['icon']} {card['title']}\n\n{card['description']}",
                use_container_width=True,
                key=f"classical_{card['page']}",
                help=f"Click to learn about {card['title']}"
            ):
                st.session_state.menu = card['page']
                st.rerun()
    
    # --- Modern Encryption Section ---
    st.markdown("<div class='section-header'>Modern Encryption</div>", unsafe_allow_html=True)
    
    # إنشاء فلاش كارد صغيرة لل Modern Encryption
    modern_cols = st.columns(2)
    for idx, card in enumerate(FLASHCARDS_DATA["modern_encryption"]):
        with modern_cols[idx]:
            if st.button(
                f"#### {card['icon']} {card['title']}\n\n{card['description']}",
                use_container_width=True,
                key=f"modern_{card['page']}",
                help=f"Click to learn about {card['title']}"
            ):
                st.session_state.menu = card['page']
                st.rerun()
    
    # --- History Section ---
    st.markdown("<div class='section-header'>History</div>", unsafe_allow_html=True)
    
    # History card in the center
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        history_card = FLASHCARDS_DATA["history"][0]
        if st.button(
            f"#### {history_card['icon']} {history_card['title']}\n\n{history_card['description']}",
            use_container_width=True,
            key=f"history_{history_card['page']}",
            help="Click to learn about cryptography history"
        ):
            st.session_state.menu = history_card['page']
            st.rerun()

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
