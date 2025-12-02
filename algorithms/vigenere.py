import streamlit as st
<<<<<<< HEAD

# ---------------- الدوال المساعدة المعدلة ----------------
def format_text(s):
    """إصدارة معدلة: تحتفظ بالحروف الإنجليزية والعربية"""
    result = []
    for c in s:
        # إنجليزية
        if ('A' <= c <= 'Z') or ('a' <= c <= 'z'):
            result.append(c.upper())
        # عربية
        elif ('ا' <= c <= 'ي') or ('أ' <= c <= 'غ'):
            result.append(c)  # العربية تحتفظ بشكلها
        # ملاحظة: الأرقام والرموز تحذف في هذه الدالة
    return ''.join(result)

def vigenere_encrypt(p, key):
    """نسخة معدلة: تشفر الإنجليزية والعربية معاً"""
    # تنظيف النص - نأخذ فقط الحروف الإنجليزية والعربية
    p_clean = ""
    for c in p:
        if ('A' <= c <= 'Z') or ('a' <= c <= 'z') or ('ا' <= c <= 'ي') or ('أ' <= c <= 'غ'):
            p_clean += c
    
    # تنظيف المفتاح - نأخذ فقط الحروف الإنجليزية من المفتاح
    key_clean = ''.join([c.upper() for c in key if ('A' <= c <= 'Z') or ('a' <= c <= 'z')])
    
    if not key_clean:
        return p  # إذا لم يكن هناك حروف إنجليزية في المفتاح
    
    res = ""
    key_index = 0
    
    for char in p_clean:
        # الإنجليزية الكبيرة
        if 'A' <= char <= 'Z':
            shift = ord(key_clean[key_index % len(key_clean)]) - 65
            res += chr((ord(char) - 65 + shift) % 26 + 65)
            key_index += 1
        # الإنجليزية الصغيرة  
        elif 'a' <= char <= 'z':
            shift = ord(key_clean[key_index % len(key_clean)]) - 65
            res += chr((ord(char) - 97 + shift) % 26 + 97)
            key_index += 1
        # العربية
        elif 'ا' <= char <= 'ي':
            arabic_start = 1575  # الألف
            arabic_end = 1610    # الياء
            shift = ord(key_clean[key_index % len(key_clean)]) - 65
            shifted_code = ((ord(char) - arabic_start + shift) % 
                           (arabic_end - arabic_start + 1)) + arabic_start
            res += chr(shifted_code)
            key_index += 1
        # العربية الخاصة
        elif 'أ' <= char <= 'غ':
            arabic_ext_start = 1571
            arabic_ext_end = 1594
            shift = ord(key_clean[key_index % len(key_clean)]) - 65
            shifted_code = ((ord(char) - arabic_ext_start + shift) % 
                           (arabic_ext_end - arabic_ext_start + 1)) + arabic_ext_start
            res += chr(shifted_code)
            key_index += 1
    
    return res

def vigenere_decrypt(c, key):
    """فك تشفير النص"""
    # تنظيف المفتاح
    key_clean = ''.join([c.upper() for c in key if ('A' <= c <= 'Z') or ('a' <= c <= 'z')])
    
    if not key_clean:
        return c
    
    res = ""
    key_index = 0
    
    for char in c:
        # الإنجليزية الكبيرة
        if 'A' <= char <= 'Z':
            shift = ord(key_clean[key_index % len(key_clean)]) - 65
            res += chr((ord(char) - 65 - shift) % 26 + 65)
            key_index += 1
        # الإنجليزية الصغيرة
        elif 'a' <= char <= 'z':
            shift = ord(key_clean[key_index % len(key_clean)]) - 65
            res += chr((ord(char) - 97 - shift) % 26 + 97)
            key_index += 1
        # العربية
        elif 'ا' <= char <= 'ي':
            arabic_start = 1575
            arabic_end = 1610
            shift = ord(key_clean[key_index % len(key_clean)]) - 65
            shifted_code = ((ord(char) - arabic_start - shift) % 
                           (arabic_end - arabic_start + 1)) + arabic_start
            res += chr(shifted_code)
            key_index += 1
        # العربية الخاصة
        elif 'أ' <= char <= 'غ':
            arabic_ext_start = 1571
            arabic_ext_end = 1594
            shift = ord(key_clean[key_index % len(key_clean)]) - 65
            shifted_code = ((ord(char) - arabic_ext_start - shift) % 
                           (arabic_extended_end - arabic_extended_start + 1)) + arabic_ext_start
            res += chr(shifted_code)
            key_index += 1
        # ملاحظة: هذا الكود لحروف فقط، الأرقام والرموز تحذف في التشفير
    
    return res

# ---------------- الإصدارة الكاملة (تدعم كل الأنواع) ----------------
def vigenere_encrypt_all(plaintext, key):
    """تشفير كامل يدعم الإنجليزية والعربية والأرقام والرموز"""
    result = ""
    key_index = 0
    
    # تنظيف المفتاح - إنجليزية فقط
    key_clean = ''.join([c.upper() for c in key if ('A' <= c <= 'Z') or ('a' <= c <= 'z')])
    if not key_clean:
        return plaintext
    
    for char in plaintext:
        # الإنجليزية الكبيرة
        if 'A' <= char <= 'Z':
            shift = ord(key_clean[key_index % len(key_clean)]) - 65
            result += chr((ord(char) - 65 + shift) % 26 + 65)
            key_index += 1
        # الإنجليزية الصغيرة
        elif 'a' <= char <= 'z':
            shift = ord(key_clean[key_index % len(key_clean)]) - 65
            result += chr((ord(char) - 97 + shift) % 26 + 97)
            key_index += 1
        # العربية (من الألف إلى الياء)
        elif 'ا' <= char <= 'ي':
            arabic_start = 1575
            arabic_end = 1610
            shift = ord(key_clean[key_index % len(key_clean)]) - 65
            shifted = ((ord(char) - arabic_start + shift) % 
                      (arabic_end - arabic_start + 1)) + arabic_start
            result += chr(shifted)
            key_index += 1
        # العربية الخاصة
        elif 'أ' <= char <= 'غ':
            arabic_ext_start = 1571
            arabic_ext_end = 1594
            shift = ord(key_clean[key_index % len(key_clean)]) - 65
            shifted = ((ord(char) - arabic_ext_start + shift) % 
                      (arabic_ext_end - arabic_ext_start + 1)) + arabic_ext_start
            result += chr(shifted)
            key_index += 1
        # الأرقام الإنجليزية
        elif '0' <= char <= '9':
            shift = ord(key_clean[key_index % len(key_clean)]) - 65
            result += chr((ord(char) - 48 + shift) % 10 + 48)
            key_index += 1
        # كل شيء آخر (رموز، مسافات، إلخ)
        else:
            result += char
            # المفتاح لا يتقدم للرموز (حسب ما تريد)
            # إذا أردت أن المفتاح يتقدم: key_index += 1
    
    return result

def vigenere_decrypt_all(ciphertext, key):
    """فك تشفير كامل"""
    result = ""
    key_index = 0
    
    key_clean = ''.join([c.upper() for c in key if ('A' <= c <= 'Z') or ('a' <= c <= 'z')])
    if not key_clean:
        return ciphertext
    
    for char in ciphertext:
        # الإنجليزية الكبيرة
        if 'A' <= char <= 'Z':
            shift = ord(key_clean[key_index % len(key_clean)]) - 65
            result += chr((ord(char) - 65 - shift) % 26 + 65)
            key_index += 1
        # الإنجليزية الصغيرة
        elif 'a' <= char <= 'z':
            shift = ord(key_clean[key_index % len(key_clean)]) - 65
            result += chr((ord(char) - 97 - shift) % 26 + 97)
            key_index += 1
        # العربية
        elif 'ا' <= char <= 'ي':
            arabic_start = 1575
            arabic_end = 1610
            shift = ord(key_clean[key_index % len(key_clean)]) - 65
            shifted = ((ord(char) - arabic_start - shift) % 
                      (arabic_end - arabic_start + 1)) + arabic_start
            result += chr(shifted)
            key_index += 1
        # العربية الخاصة
        elif 'أ' <= char <= 'غ':
            arabic_ext_start = 1571
            arabic_ext_end = 1594
            shift = ord(key_clean[key_index % len(key_clean)]) - 65
            shifted = ((ord(char) - arabic_ext_start - shift) % 
                      (arabic_ext_end - arabic_ext_start + 1)) + arabic_ext_start
            result += chr(shifted)
            key_index += 1
        # الأرقام الإنجليزية
        elif '0' <= char <= '9':
            shift = ord(key_clean[key_index % len(key_clean)]) - 65
            result += chr((ord(char) - 48 - shift) % 10 + 48)
            key_index += 1
        # كل شيء آخر
        else:
            result += char
            # إذا أردت أن المفتاح يتقدم: key_index += 1
    
    return result

# ---------------- صفحة Vigenère ----------------
def show_vigenere_page():
    # ... نفس CSS السابق ...
    
    # في الأزرار، اختر أي نسخة تريد:
    
    # النسخة البسيطة (للحروف فقط):
    # encrypted = vigenere_encrypt(text, key)
    
    # النسخة الكاملة (لكل الأنواع):
    # encrypted = vigenere_encrypt_all(text, key)
    
    pass
=======
import base64

# ==== Vigenère UTF-8 Encryption / Decryption ====
def vigenere_encrypt_utf8(plaintext, key):
    plaintext_bytes = plaintext.encode("utf-8")
    key_bytes = key.encode("utf-8")
    encrypted_bytes = bytearray()
    for i in range(len(plaintext_bytes)):
        encrypted_bytes.append((plaintext_bytes[i] + key_bytes[i % len(key_bytes)]) % 256)
    return base64.b64encode(encrypted_bytes).decode()

def vigenere_decrypt_utf8(ciphertext_b64, key):
    ciphertext_bytes = base64.b64decode(ciphertext_b64)
    key_bytes = key.encode("utf-8")
    decrypted_bytes = bytearray()
    for i in range(len(ciphertext_bytes)):
        decrypted_bytes.append((ciphertext_bytes[i] - key_bytes[i % len(key_bytes)]) % 256)
    return decrypted_bytes.decode("utf-8")

# ==== Streamlit Page ====
def show_vigenere_page():
    st.markdown("""
    <style>
    body {background: linear-gradient(135deg, #0b0c10, #1c1f2a); color: #e0e0e0; font-family: 'Inter', sans-serif;}
    .vig-card {background: rgba(255,255,255,0.03); backdrop-filter: blur(16px); border-radius: 25px; padding: 25px; margin-bottom: 30px;
               box-shadow: 0 6px 18px rgba(0,0,0,0.25); transition: transform 0.3s ease, box-shadow 0.3s ease;}
    .vig-card:hover {transform: translateY(-8px); box-shadow: 0 14px 32px rgba(0,0,0,0.35);}
    .vig-title {color: #a8c0ff; font-size: 24px; font-weight: 700; margin-bottom: 15px;}
    .vig-output {background: rgba(255,255,255,0.05); padding: 12px; border-radius: 15px; font-family: monospace; color: #fff;
                 margin-top: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.2); word-break: break-all;}
    .vig-btn {background: linear-gradient(90deg, #627daa, #a8c0ff); border: none; color: white; font-weight: 600;
              padding: 12px 28px; border-radius: 15px; cursor: pointer; transition: all 0.3s ease; margin-top: 12px; font-size: 16px;}
    .vig-btn:hover {background: linear-gradient(90deg, #a8c0ff, #fbc2eb); transform: scale(1.08); box-shadow: 0 8px 24px rgba(168,192,255,0.4);}
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color:#a8c0ff; font-weight:700; margin-bottom:25px;">Vigenère Cipher UTF-8</h1>', unsafe_allow_html=True)

    # Encryption
    st.markdown('<div class="vig-card">', unsafe_allow_html=True)
    st.markdown('<div class="vig-title">Encryption</div>', unsafe_allow_html=True)
    plaintext = st.text_area("Plaintext")
    key = st.text_input("Key")
    if st.button("Encrypt"):
        if plaintext and key:
            encrypted = vigenere_encrypt_utf8(plaintext, key)
            st.markdown(f'<div class="vig-output">{encrypted}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Decryption
    st.markdown('<div class="vig-card">', unsafe_allow_html=True)
    st.markdown('<div class="vig-title">Decryption</div>', unsafe_allow_html=True)
    ciphertext = st.text_area("Ciphertext (Base64)")
    key2 = st.text_input("Key for Decryption")
    if st.button("Decrypt"):
        if ciphertext and key2:
            try:
                decrypted = vigenere_decrypt_utf8(ciphertext, key2)
                st.markdown(f'<div class="vig-output">{decrypted}</div>', unsafe_allow_html=True)
            except:
                st.error("Invalid ciphertext or key")
    st.markdown('</div>', unsafe_allow_html=True)
>>>>>>> cdbb208b9536a8c7ce52044e5b369d4d4985633d
