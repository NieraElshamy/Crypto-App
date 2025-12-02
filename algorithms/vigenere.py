import streamlit as st

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