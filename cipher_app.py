import encryption as enc
import senddata as sd


def get_user_input():
    print("\nKullanılabilir Şifreleme Algoritmaları:")
    print("1. Sezar Şifreleme")
    print("2. Doğrusal Şifreleme")
    print("3. Yerdeğiştirme Şifreleme")
    print("4. Permutasyon Şifreleme")
    print("5. Rota Şifreleme")
    print("6. Zigzag Şifreleme")
    print("7. Vigenere Şifreleme")
    print("8. 4 Kare Şifreleme")
    print("9. Hill Şifreleme")
    
    while True:
        try:
            choice = int(input("\nŞifreleme algoritması seçin (1-9): "))
            if 1 <= choice <= 9:
                break
            print("Lütfen 1-9 arasında bir sayı girin.")
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")
    
    text = input("Şifrelenecek metni girin: ")
    
    if choice == 1:  # Sezar
        shift = int(input("Kaydırma miktarını girin (1-25): "))
        return choice, text, shift
    
    elif choice == 2:  # Doğrusal
        a = int(input("a değerini girin (1-25): "))
        b = int(input("b değerini girin (1-25): "))
        return choice, text, (a, b)
    
    elif choice == 3:  # Yerdeğiştirme
        key = input("Anahtar kelimeyi girin (26 farklı harf içermeli): ").upper()
        return choice, text, key
    
    elif choice == 4:  # Permutasyon
        key_str = input("Permutasyon anahtarını girin (örn: 3,1,4,2): ")
        key = [int(x) for x in key_str.split(',')]
        return choice, text, key
    
    elif choice == 5:  # Rota
        rows = int(input("Matris satır sayısını girin: "))
        cols = int(input("Matris sütun sayısını girin: "))
        return choice, text, (rows, cols)
    
    elif choice == 6:  # Zigzag
        rows = int(input("Zigzag satır sayısını girin: "))
        return choice, text, rows
    
    elif choice == 7:  # Vigenere
        key = input("Anahtar kelimeyi girin: ").upper()
        return choice, text, key
    
    elif choice == 8:  # 4 Kare
        key1 = input("Birinci anahtar kelimeyi girin: ").upper()
        key2 = input("İkinci anahtar kelimeyi girin: ").upper()
        return choice, text, (key1, key2)
    
    elif choice == 9:  # Hill
        size = int(input("Matris boyutunu girin (2 veya 3): "))
        print(f"{size}x{size} matris elemanlarını girin (her satır için virgülle ayrılmış):")
        key = []
        for i in range(size):
            row = input(f"{i+1}. satır: ")
            key.append([int(x) for x in row.split(',')])
        return choice, text, key

def main():
    while True:
        print("\n=== Şifreleme Programı ===")
        print("1. Şifrele")
        print("2. Çıkış")
        
        try:
            operation = int(input("İşlem seçin (1-2): "))
            if operation == 2:
                print("Program sonlandırılıyor...")
                break
            if operation not in [1, 2]:
                print("Geçersiz seçim. Lütfen 1-2 arasında bir sayı girin.")
                continue
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")
            continue
        
        choice, text, key = get_user_input()
        
        try:
            if operation == 1:
                result = enc.encrypt_text(choice, text, key)
                print(f"\nŞifreli Metin: {enc.data_send}")

                send_option = input("Şifreli metni gönder. (e/h): ").strip().lower()
                if send_option == 'e':
                    sd.send_encrypted_message(choice,result,key)
                    print("Mesaj gönderildi.")

        except Exception as e:
            print(f"Hata oluştu: {str(e)}")
        
        input("\nDevam etmek için Enter'a basın...")

if __name__ == "__main__":
    main() 