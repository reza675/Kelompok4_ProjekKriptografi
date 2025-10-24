#Kelompok 4:
# 1. Adi Setya Nur Pradipta (123230026)
# 2. Reza Rasendriya Adi Putra (123230030)
# 3. Muhammad David Firdaus (123230039)
# 4. Gusti Rama (123230040)
#Kelas: IF-B

import streamlit as st

from algoritma import (
    caesar_enkripsi, caesar_dekripsi,
    railfence_enkripsi, railfence_dekripsi,
    xor_encrypt_decrypt,
    rc4_enkripsi, rc4_dekripsi,
    super_encrypt, super_decrypt
)

st.set_page_config(page_title="Kelompok 4 Kriptografi", page_icon="🔐", layout="wide")

# ==================== CUSTOM CSS ====================  
st.markdown("""
<style>
    body { font-family: 'Segoe UI', sans-serif; }
    .main-header { font-size: 2.5rem; color: #1f77b4; text-align: center; margin-bottom: .25rem; }
    .sub-header { text-align:center; color:#6b7280; margin-bottom: 1rem; }
    .muted { color:#6b7280; font-size:.9rem; }
    .hint { color:#4b5563; font-size:.85rem; }
    .result { background:#0b1020; color:#e5e7eb; padding:.75rem 1rem; border-radius:10px; }
    
    div.stButton > button { 
        border-radius:10px; 
        border:0; 
        background-color:#1f77b4 !important; 
        color:#ffffff !important; 
        box-shadow:0 6px 14px rgba(31,119,180,.25); 
    }
    div.stButton > button:hover { 
        background-color:#155fa0 !important; 
        box-shadow:0 8px 18px rgba(21,95,160,.28); 
    }
    div.stButton > button:focus { outline:2px solid #93c5fd; }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="main-header">🔐 Kriptografi Klasik dan Modern</h1>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Tugas 4 Kriptografi Klasik dan Modern</div>', unsafe_allow_html=True)
    st.markdown("---")

    st.sidebar.title("🔧 Pilih Cipher")
    cipher_choice = st.sidebar.radio(
        "Pilih algoritma:",
        ["🏛️ Caesar Cipher", "🚂 Rail Fence Cipher", "⚡ XOR Cipher", "🔄 RC4 Cipher", "🌀 Super Encryption"]
    )

    st.sidebar.markdown("---")
    st.sidebar.title("ℹ️ Tentang")
    st.sidebar.info("""
**Jenis-Jenis Cipher Dalam Tugas Ini:**
- **Caesar Cipher** (Klasik): Menggeser huruf dengan kunci tertentu.
- **Rail Fence Cipher** (Klasik): Menyusun teks secara zigzag di beberapa "rel".
- **XOR Cipher** (Modern sederhana): Operasi XOR dengan kunci numerik.
- **RC4 Cipher** (Modern): Stream cipher berbasis keystream pseudorandom.
""")

    if "Caesar" in cipher_choice: caesar_ui()
    elif "Rail" in cipher_choice: railfence_ui()
    elif "XOR" in cipher_choice: xor_ui()
    elif "RC4" in cipher_choice: rc4_ui()
    elif "Super" in cipher_choice: super_ui()

    st.markdown("---")

def caesar_ui():
    st.markdown('<div class="cipher-section">', unsafe_allow_html=True)
    st.header("🏛️ Caesar Cipher")
    st.caption("Geser huruf berdasarkan kunci pergeseran.")
    col1, col2 = st.columns([1.1, 1])
    with col1:
        text = st.text_area("Teks input", height=120, help="Masukkan teks huruf A-Z/a-z.")
        key = st.number_input("Kunci pergeseran", min_value=1, max_value=25, value=3)
        encrypt_tab, decrypt_tab = st.tabs(["🔒 Enkripsi", "🔓 Dekripsi"])
        with encrypt_tab:
            enc_click = st.button("Jalankan Enkripsi Caesar")
        with decrypt_tab:
            dec_click = st.button("Jalankan Dekripsi Caesar")
    with col2:
        st.markdown("Hasil:")
        if 'enc_click' in locals() and enc_click:
            st.code(caesar_enkripsi(text, key), language=None)
        elif 'dec_click' in locals() and dec_click:
            st.code(caesar_dekripsi(text, key), language=None)
    st.markdown('</div>', unsafe_allow_html=True)

def railfence_ui():
    st.markdown('<div class="cipher-section">', unsafe_allow_html=True)
    st.header("🚂 Rail Fence Cipher")
    st.caption("Susun teks secara zigzag di beberapa rel untuk menyamarkan urutan.")
    col1, col2 = st.columns([1.1, 1])
    with col1:
        text = st.text_area("Teks input", height=120)
        rails = st.number_input("Jumlah rel", min_value=2, max_value=10, value=3)
        encrypt_tab, decrypt_tab = st.tabs(["🔒 Enkripsi", "🔓 Dekripsi"])
        with encrypt_tab:
            enc_click = st.button("Jalankan Enkripsi Rail Fence")
        with decrypt_tab:
            dec_click = st.button("Jalankan Dekripsi Rail Fence")
    with col2:
        st.markdown("Hasil:")
        if 'enc_click' in locals() and enc_click:
            st.code(railfence_enkripsi(text, rails), language=None)
        elif 'dec_click' in locals() and dec_click:
            st.code(railfence_dekripsi(text, rails), language=None)
    st.markdown('</div>', unsafe_allow_html=True)

def xor_ui():
    st.markdown('<div class="cipher-section">', unsafe_allow_html=True)
    st.header("⚡ XOR Cipher")
    st.caption("Operasi XOR per karakter dengan kunci numerik yang sama untuk enkripsi/dekripsi.")
    col1, col2 = st.columns([1.1, 1])
    with col1:
        text = st.text_area("Teks input", height=120)
        key = st.number_input("Kunci XOR (1-255)", min_value=1, max_value=255, value=42)
        encrypt_tab, decrypt_tab = st.tabs(["🔒 Enkripsi", "🔓 Dekripsi"])
        with encrypt_tab:
            enc_click = st.button("Jalankan Enkripsi XOR")
        with decrypt_tab:
            dec_click = st.button("Jalankan Dekripsi XOR")
    with col2:
        st.markdown("Hasil:")
        if 'enc_click' in locals() and enc_click:
            st.code(xor_encrypt_decrypt(text, key), language=None)
        elif 'dec_click' in locals() and dec_click:
            st.code(xor_encrypt_decrypt(text, key), language=None)
    st.markdown('</div>', unsafe_allow_html=True)

def rc4_ui():
    st.markdown('<div class="cipher-section">', unsafe_allow_html=True)
    st.header("🔄 RC4 Cipher")
    st.caption("Stream cipher yang menghasilkan keystream pseudorandom untuk XOR dengan plaintext.")
    col1, col2 = st.columns([1.1, 1])
    with col1:
        text = st.text_area("Teks input", height=120)
        key = st.text_input("Kunci rahasia", value="secretkey")
        encrypt_tab, decrypt_tab = st.tabs(["🔒 Enkripsi", "🔓 Dekripsi"])
        with encrypt_tab:
            enc_click = st.button("Jalankan Enkripsi RC4")
        with decrypt_tab:
            dec_click = st.button("Jalankan Dekripsi RC4")
    with col2:
        st.markdown("Hasil:")
        if 'enc_click' in locals() and enc_click:
            st.code(rc4_enkripsi(text, key), language=None)
        elif 'dec_click' in locals() and dec_click:
            st.code(rc4_dekripsi(text, key), language=None)
    st.markdown('</div>', unsafe_allow_html=True)

def super_ui(): 
    st.markdown('<div class="cipher-section">', unsafe_allow_html=True) 
    st.header("🌀 Super Encryption (Caesar → Rail Fence → RC4 → XOR)") 
    st.caption("Kombinasi berantai: Caesar → Rail Fence → RC4 → XOR untuk menyamarkan pesan.") 
    col1, col2 = st.columns([1.1, 1])
    with col1:
        text = st.text_area("Teks input", height=120) 
        caesar_shift = st.number_input("Caesar shift", min_value=1, max_value=25, value=3)
        rails = st.number_input("Jumlah rel (Rail Fence)", min_value=2, max_value=10, value=3) 
        rc4_key = st.text_input("Kunci RC4", value="secretkey") 
        xor_key = st.number_input("Kunci XOR", min_value=1, max_value=255, value=42) 
        encrypt_tab, decrypt_tab = st.tabs(["🔒 Enkripsi", "🔓 Dekripsi"]) 
        with encrypt_tab: 
            enc_click = st.button("Jalankan Super Encryption") 
        with decrypt_tab: 
            dec_click = st.button("Jalankan Super Decryption") 
    with col2:
        st.markdown("Hasil:")
        if 'enc_click' in locals() and enc_click:
            st.code(super_encrypt(text, caesar_shift, rails, rc4_key, xor_key), language=None) 
        elif 'dec_click' in locals() and dec_click:
            st.code(super_decrypt(text, caesar_shift, rails, rc4_key, xor_key), language=None) 
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
