from cipher_suite import CipherSuite

def main():
    # Sezar şifreleme örneği
    text = "Merhaba Dünya"
    shift = 3
    encrypted = CipherSuite.caesar_encrypt(text, shift)
    decrypted = CipherSuite.caesar_decrypt(encrypted, shift)
    print(f"Sezar Şifreleme:")
    print(f"Orijinal: {text}")
    print(f"Şifreli: {encrypted}")
    print(f"Çözülmüş: {decrypted}\n")

    # Doğrusal şifreleme örneği
    a, b = 5, 7
    encrypted = CipherSuite.linear_encrypt(text, a, b)
    decrypted = CipherSuite.linear_decrypt(encrypted, a, b)
    print(f"Doğrusal Şifreleme:")
    print(f"Orijinal: {text}")
    print(f"Şifreli: {encrypted}")
    print(f"Çözülmüş: {decrypted}\n")

    # Yerdeğiştirme şifreleme örneği
    key = "QWERTYUIOPASDFGHJKLZXCVBNM"
    encrypted = CipherSuite.substitution_encrypt(text, key)
    decrypted = CipherSuite.substitution_decrypt(encrypted, key)
    print(f"Yerdeğiştirme Şifreleme:")
    print(f"Orijinal: {text}")
    print(f"Şifreli: {encrypted}")
    print(f"Çözülmüş: {decrypted}\n")

    # Permutasyon şifreleme örneği
    key = [3, 1, 4, 2]
    encrypted = CipherSuite.permutation_encrypt(text, key)
    decrypted = CipherSuite.permutation_decrypt(encrypted, key)
    print(f"Permutasyon Şifreleme:")
    print(f"Orijinal: {text}")
    print(f"Şifreli: {encrypted}")
    print(f"Çözülmüş: {decrypted}\n")

    # Rota şifreleme örneği
    rows, cols = 3, 4
    encrypted = CipherSuite.route_encrypt(text, rows, cols)
    decrypted = CipherSuite.route_decrypt(encrypted, rows, cols)
    print(f"Rota Şifreleme:")
    print(f"Orijinal: {text}")
    print(f"Şifreli: {encrypted}")
    print(f"Çözülmüş: {decrypted}\n")

    # Zigzag şifreleme örneği
    rows = 3
    encrypted = CipherSuite.zigzag_encrypt(text, rows)
    decrypted = CipherSuite.zigzag_decrypt(encrypted, rows)
    print(f"Zigzag Şifreleme:")
    print(f"Orijinal: {text}")
    print(f"Şifreli: {encrypted}")
    print(f"Çözülmüş: {decrypted}\n")

    # Vigenere şifreleme örneği
    key = "KEY"
    encrypted = CipherSuite.vigenere_encrypt(text, key)
    decrypted = CipherSuite.vigenere_decrypt(encrypted, key)
    print(f"Vigenere Şifreleme:")
    print(f"Orijinal: {text}")
    print(f"Şifreli: {encrypted}")
    print(f"Çözülmüş: {decrypted}\n")

    # 4 Kare şifreleme örneği
    key1 = "KEYWORD"
    key2 = "SECRET"
    encrypted = CipherSuite.four_square_encrypt(text, key1, key2)
    decrypted = CipherSuite.four_square_decrypt(encrypted, key1, key2)
    print(f"4 Kare Şifreleme:")
    print(f"Orijinal: {text}")
    print(f"Şifreli: {encrypted}")
    print(f"Çözülmüş: {decrypted}\n")

    # Hill şifreleme örneği
    key = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
    encrypted = CipherSuite.hill_encrypt(text, key)
    decrypted = CipherSuite.hill_decrypt(encrypted, key)
    print(f"Hill Şifreleme:")
    print(f"Orijinal: {text}")
    print(f"Şifreli: {encrypted}")
    print(f"Çözülmüş: {decrypted}\n")

if __name__ == "__main__":
    main() 