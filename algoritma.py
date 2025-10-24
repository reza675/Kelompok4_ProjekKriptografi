def RC4_penjadwalan_kunci(kunci):
    jadwal = [i for i in range(256)]
    indeks_i = 0
    for indeks_j in range(256):
        indeks_i = (indeks_i + jadwal[indeks_j] + kunci[indeks_j % len(kunci)]) % 256
        jadwal[indeks_j], jadwal[indeks_i] = jadwal[indeks_i], jadwal[indeks_j]
    return jadwal

def RC4_stream_generation(jadwal):
    indeks_i = 0
    indeks_j = 0
    while True:
        indeks_i = (indeks_i + 1) % 256
        indeks_j = (jadwal[indeks_i] + indeks_j) % 256
        jadwal[indeks_i], jadwal[indeks_j] = jadwal[indeks_j], jadwal[indeks_i]
        yield jadwal[(jadwal[indeks_i] + jadwal[indeks_j]) % 256]

def rc4_enkripsi(teks, kunci):
    teks = [ord(c) for c in teks]
    kunci = [ord(c) for c in kunci]
    jadwal = RC4_penjadwalan_kunci(kunci)
    aliran_kunci = RC4_stream_generation(jadwal)
    return "".join(str(hex(c ^ next(aliran_kunci))).upper() for c in teks)

def rc4_dekripsi(teks_sandi, kunci):
    bagian_hex = teks_sandi.split("0X")[1:]
    bagian_hex = [int("0x" + b.lower(), 0) for b in bagian_hex]
    kunci = [ord(c) for c in kunci]
    jadwal = RC4_penjadwalan_kunci(kunci)
    aliran_kunci = RC4_stream_generation(jadwal)
    return "".join(chr(c ^ next(aliran_kunci)) for c in bagian_hex)

def caesar_enkripsi(message, key):
    encrypted = ""
    for c in message:
        if c.isalpha():
            if c.islower():
                encrypted += chr((ord(c) - ord('a') + key) % 26 + ord('a'))
            else:
                encrypted += chr((ord(c) - ord('A') + key) % 26 + ord('A'))
        else:
            encrypted += c
    return encrypted

def caesar_dekripsi(message, key):
    decrypted = ""
    for c in message:
        if c.isalpha():
            if c.islower():
                decrypted += chr((ord(c) - ord('a') - key) % 26 + ord('a'))
            else:
                decrypted += chr((ord(c) - ord('A') - key) % 26 + ord('A'))
        else:
            decrypted += c
    return decrypted

def railfence_enkripsi(text, key):
    rail = [["\n" for _ in range(len(text))] for _ in range(key)]
    direction_bwh, row, col = False, 0, 0
    for char in text:
        if row == 0 or row == key - 1:
            direction_bwh = not direction_bwh
        rail[row][col] = char
        col += 1
        row = row + 1 if direction_bwh else row - 1
    return "".join(rail[i][j] for i in range(key) for j in range(len(text)) if rail[i][j] != "\n")

def railfence_dekripsi(cipher, key):
    rail = [["\n" for _ in range(len(cipher))] for _ in range(key)]
    direction_bwh, row, col = None, 0, 0
    for _ in cipher:
        direction_bwh = True if row == 0 else False if row == key - 1 else direction_bwh
        rail[row][col] = "*"; col += 1
        row = row + 1 if direction_bwh else row - 1
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == "*" and index < len(cipher):
                rail[i][j] = cipher[index]; index += 1
    result, row, col, direction_bwh = [], 0, 0, None
    for _ in cipher:
        direction_bwh = True if row == 0 else False if row == key - 1 else direction_bwh
        if rail[row][col] != "*":
            result.append(rail[row][col]); col += 1
        row = row + 1 if direction_bwh else row - 1
    return "".join(result)

def xor_encrypt_decrypt(input_string, key):
    return "".join(chr(ord(c) ^ key) for c in input_string)

def super_encrypt(plaintext, caesar_shift, rails, rc4_key, xor_key): 
    #Step 1: Caesar Cipher 
    step1 = caesar_enkripsi(plaintext, caesar_shift) 
    #Step 2: Rail Fence Cipher 
    step2 = railfence_enkripsi(step1, rails) 
    #Step 3: RC4 
    step3 = rc4_enkripsi(step2, rc4_key) 
    #Step 4: XOR (hasil RC4 masih hex, jadi langsung pakai string XOR) 
    step4 = xor_encrypt_decrypt(step3, xor_key) 
    return step4 

def super_decrypt(ciphertext, caesar_shift, rails, rc4_key, xor_key): 
    #Step 1: XOR balik 
    step1 = xor_encrypt_decrypt(ciphertext, xor_key) 
    #Step 2: RC4 dekripsi 
    step2 = rc4_dekripsi(step1, rc4_key) 
    #Step 3: Rail Fence dekripsi 
    step3 = railfence_dekripsi(step2, rails) 
    #Step 4: Caesar dekripsi 
    step4 = caesar_dekripsi(step3, caesar_shift) 
    return step4
