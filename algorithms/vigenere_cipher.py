
import streamlit as st


def get_shift_value(key_char):
    """Get shift value from key character - CORRECTED"""
    # Convert key character to uppercase FIRST
    if 'A' <= key_char.upper() <= 'Z':
        return ord(key_char.upper()) - ord('A')
    
    elif '\u0621' <= key_char <= '\u064A':
        arabic_alphabet = 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي'
        if key_char in arabic_alphabet:
            return arabic_alphabet.index(key_char)
        else:
            return (ord(key_char) - ord('\u0621')) % 28
    
    elif '0' <= key_char <= '9':
        return int(key_char)
    
    
    else:
        return ord(key_char) % 26

def vigenere_encrypt(text: str, key: str) -> str:
    """Encrypt text using Vigenère cipher - FINAL CORRECTION"""
    if not key or not text:
        return text
    
    result = []
    key_index = 0
    key_length = len(key)
    
    for char in text:
        
        is_upper = 'A' <= char <= 'Z'
        is_lower = 'a' <= char <= 'z'
        
        if is_upper or is_lower:  
            key_char = key[key_index % key_length]
            shift = get_shift_value(key_char)
            
            if is_upper:
                base = ord('A')
                encrypted = chr((ord(char) - base + shift) % 26 + base)
            else:  
                base = ord('a')
                encrypted = chr((ord(char) - base + shift) % 26 + base)
            
            result.append(encrypted)
            key_index += 1  
            
        elif '\u0621' <= char <= '\u064A':  
            arabic_alphabet = 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي'
            if char in arabic_alphabet:
                key_char = key[key_index % key_length]
                shift = get_shift_value(key_char)
                char_index = arabic_alphabet.index(char)
                encrypted_index = (char_index + shift) % 28
                encrypted = arabic_alphabet[encrypted_index]
                result.append(encrypted)
                key_index += 1
            else:
                result.append(char)
                
        elif '0' <= char <= '9':  
            key_char = key[key_index % key_length]
            shift = get_shift_value(key_char)
            base = ord('0')
            shift_mod = shift % 10
            encrypted = chr((ord(char) - base + shift_mod) % 10 + base)
            result.append(encrypted)
            key_index += 1
            
        else:  
            result.append(char)
    
    return ''.join(result)

def vigenere_decrypt(cipher: str, key: str) -> str:
    """Decrypt text using Vigenère cipher - FINAL CORRECTION"""
    if not key or not cipher:
        return cipher
    
    result = []
    key_index = 0
    key_length = len(key)
    
    for char in cipher:
        is_upper = 'A' <= char <= 'Z'
        is_lower = 'a' <= char <= 'z'
        
        if is_upper or is_lower:  
            key_char = key[key_index % key_length]
            shift = get_shift_value(key_char)
            
            if is_upper:
                base = ord('A')
                decrypted = chr((ord(char) - base - shift) % 26 + base)
            else: 
                base = ord('a')
                decrypted = chr((ord(char) - base - shift) % 26 + base)
            
            result.append(decrypted)
            key_index += 1
            
        elif '\u0621' <= char <= '\u064A':  
            arabic_alphabet = 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي'
            if char in arabic_alphabet:
                key_char = key[key_index % key_length]
                shift = get_shift_value(key_char)
                char_index = arabic_alphabet.index(char)
                shift_mod = shift % 28
                decrypted_index = (char_index - shift_mod) % 28
                decrypted = arabic_alphabet[decrypted_index]
                result.append(decrypted)
                key_index += 1
            else:
                result.append(char)
                
        elif '0' <= char <= '9':  
            key_char = key[key_index % key_length]
            shift = get_shift_value(key_char)
            base = ord('0')
            shift_mod = shift % 10
            decrypted = chr((ord(char) - base - shift_mod) % 10 + base)
            result.append(decrypted)
            key_index += 1
            
        else:  
            result.append(char)
    
    return ''.join(result)

