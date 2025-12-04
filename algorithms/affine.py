import streamlit as st
import math

# --- 1. دوال شفرة الأفّاين الأساسية ---

M = 26 # حجم الأبجدية الإنجليزية

def get_mod_inverse(a, m):
    """تحسب المعكوس الضربي المعياري لـ a بالنسبة لـ m."""
    # يتطلب أن يكون القاسم المشترك الأكبر (gcd) لـ (a, m) يساوي 1
    if math.gcd(a, m) != 1:
        return None
    
    # استخدام pow(a, -1, m) لحساب المعكوس الضربي المعياري (في بايثون 3.8 فما فوق)
    # العودة إلى البحث التقليدي إذا فشلت دالة pow (للإصدارات الأقدم من بايثون)
    try:
        if pow(a, 1, m) == 0: # التحقق مما إذا كان a مضاعفاً لـ m
            return None
        return pow(a, -1, m)
    except TypeError:
        # البحث التقليدي للإصدارات الأقدم من بايثون
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

def encrypt_affine(plaintext, a, b):
    """تقوم بتشفير النص العادي باستخدام E(x) = (ax + b) mod 26"""
    ciphertext = ""
    # التكرار على كل حرف وتحويله إلى حرف كبير (uppercase)
    for char in plaintext.upper():
        if 'A' <= char <= 'Z':
            x = ord(char) - ord('A')
            y = (a * x + b) % M
            ciphertext += chr(y + ord('A'))
        else:
            # الاحتفاظ بالرموز الأخرى كما هي
            ciphertext += char
    return ciphertext

def decrypt_affine(ciphertext, a, b):
    """تقوم بفك تشفير النص المشفر باستخدام D(y) = a^-1(y - b) mod 26"""
    # يتم حساب المعكوس والتحقق منه في منطق واجهة المستخدم (متغير a_inverse)
    a_inverse = get_mod_inverse(a, M)
    
    if a_inverse is None:
        # يجب أن يتم التعامل مع هذه الحالة بواسطة واجهة المستخدم قبل استدعاء الدالة
        pass 

    plaintext = ""
    for char in ciphertext.upper():
        if 'A' <= char <= 'Z':
            y = ord(char) - ord('A')
            # يتم استخدام المعكوس الصالح في عملية فك التشفير
            x = (a_inverse * (y - b)) % M
            plaintext += chr(x + ord('A'))
        else:
            plaintext += char
    return plaintext

# --- 2. تصميم واجهة Streamlit ---

st.set_page_config(page_title="Affine Cipher App", layout="centered")
st.title("Affine Cipher Web Application")
st.markdown("Text is converted to uppercase, and spaces, numbers, and symbols are ignored during encryption/decryption.")
st.markdown("---")

# --- إدخال المفاتيح في الشريط الجانبي (English UI) ---

st.sidebar.header("Key Settings (M=26)")
st.sidebar.info("Key A must be coprime with 26 (i.e., gcd(A, 26) = 1). Valid keys are: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25.")

# مدخلات الأرقام (English Labels)
key_a = st.sidebar.number_input("Key A (Multiplier):", min_value=1, max_value=25, value=5, step=1)
key_b = st.sidebar.number_input("Key B (Shift):", min_value=0, max_value=25, value=8, step=1)

# التحقق من صلاحية المفتاح A وعرض المعكوس (English Messages)
a_inverse = get_mod_inverse(key_a, M)
if a_inverse is None:
    st.sidebar.error("Key A is invalid. Decryption will fail.")
else:
    st.sidebar.success(f"Key A is valid. Modular Inverse (A⁻¹): {a_inverse}")


# --- منطقة إدخال النص (English Label) ---
input_text = st.text_area("Enter Text Here:", "The Affine Cipher is a type of monoalphabetic substitution cipher.", height=150)

# --- الأزرار والنتائج (English Labels and Messages) ---
col1, col2 = st.columns(2)

with col1:
    if st.button('Encrypt', use_container_width=True):
        if a_inverse is None:
            st.error("Cannot encrypt with an invalid key A for decryption.")
        else:
            cipher = encrypt_affine(input_text, key_a, key_b)
            st.success("Ciphertext:")
            st.code(cipher)

with col2:
    if st.button('Decrypt', use_container_width=True):
        if a_inverse is None:
            st.error("Cannot decrypt. Key A is invalid.")
        else:
            plaintext = decrypt_affine(input_text, key_a, key_b)
            st.info("Decrypted Plaintext:")
            st.code(plaintext)

st.markdown("---")
st.caption("Application developed using Streamlit and the Affine Cipher.")
