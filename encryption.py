from cipher_suite import CipherSuite

data_send = "0şifreatanmadı0"

def encrypt_text(choice, text, key):
    """Seçilen algoritmaya göre metni şifreler"""

    global data_send
    if choice == 1:  # Sezar
        data_send = CipherSuite.caesar_encrypt(text, key)
        return data_send
    elif choice == 2:  # Doğrusal
        a, b = key
        data_send = CipherSuite.linear_encrypt(text, a, b)
        return data_send
    elif choice == 3:  # Yerdeğiştirme
        data_send = CipherSuite.substitution_encrypt(text, key)
        return data_send
    elif choice == 4:  # Permutasyon
        data_send = CipherSuite.permutation_encrypt(text, key)
        return data_send
    elif choice == 5:  # Rota
        rows, cols = key
        data_send = CipherSuite.route_encrypt(text, rows, cols)
        return data_send
    elif choice == 6:  # Zigzag
        data_send = CipherSuite.zigzag_encrypt(text, key)
        return data_send
    elif choice == 7:  # Vigenere
        data_send = CipherSuite.vigenere_encrypt(text, key)
        return data_send
    elif choice == 8:  # 4 Kare
        key1, key2 = key
        data_send = CipherSuite.four_square_encrypt(text, key1, key2)
        return data_send
    elif choice == 9:  # Hill
        data_send = CipherSuite.hill_encrypt(text, key)
        return data_send
    else:
        raise ValueError("Geçersiz şifreleme algoritması seçimi") 