import numpy as np
from typing import List, Tuple


class CipherSuite:
    @staticmethod
    def caesar_encrypt(text: str, shift: int) -> str:
        """Sezar şifreleme algoritması"""
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                result += char
        return result

    @staticmethod
    def linear_encrypt(text: str, a: int, b: int) -> str:
        """Doğrusal şifreleme algoritması"""
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                x = ord(char) - ascii_offset
                result += chr((a * x + b) % 26 + ascii_offset)
            else:
                result += char
        return result

    @staticmethod
    def substitution_encrypt(text: str, key: str) -> str:
        """Yerdeğiştirme şifreleme algoritması"""
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        key = key.upper()
        result = ""
        for char in text:
            if char.isalpha():
                is_upper = char.isupper()
                char = char.upper()
                if char in alphabet:
                    index = alphabet.index(char)
                    new_char = key[index]
                    result += new_char if is_upper else new_char.lower()
            else:
                result += char
        return result

    @staticmethod
    def permutation_encrypt(text: str, key: List[int]) -> str:
        """Permutasyon şifreleme algoritması"""
        # Metni bloklara böl
        block_size = len(key)
        text = text.upper()
        # Boşlukları kaldır
        text = ''.join(text.split())
        # Metni bloklara böl
        blocks = [text[i:i+block_size] for i in range(0, len(text), block_size)]
        result = ""
        for block in blocks:
            # Eksik karakterleri doldur
            if len(block) < block_size:
                block += 'X' * (block_size - len(block))
            # Permutasyon uygula
            permuted = ''.join([block[i-1] for i in key])
            result += permuted
        return result

    @staticmethod
    def route_encrypt(text: str, rows: int, cols: int) -> str:
        """Rota şifreleme algoritması"""
        # Metni matrise yerleştir
        text = text.upper()
        # Boşlukları kaldır
        text = ''.join(text.split())
        # Eksik karakterleri doldur
        while len(text) < rows * cols:
            text += 'X'
        # Matrisi oluştur
        matrix = [list(text[i*cols:(i+1)*cols]) for i in range(rows)]
        # Spiral okuma
        result = ""
        top, bottom, left, right = 0, rows-1, 0, cols-1
        while top <= bottom and left <= right:
            # Sağa
            for i in range(left, right+1):
                result += matrix[top][i]
            top += 1
            # Aşağı
            for i in range(top, bottom+1):
                result += matrix[i][right]
            right -= 1
            if top <= bottom:
                # Sola
                for i in range(right, left-1, -1):
                    result += matrix[bottom][i]
                bottom -= 1
            if left <= right:
                # Yukarı
                for i in range(bottom, top-1, -1):
                    result += matrix[i][left]
                left += 1
        return result


    @staticmethod
    def zigzag_encrypt(text: str, rows: int) -> str:
        """Zigzag şifreleme algoritması"""
        if rows == 1:
            return text
        # Boşlukları kaldır
        text = ''.join(text.split())
        # Zigzag matrisi oluştur
        matrix = [[''] * len(text) for _ in range(rows)]
        row, col = 0, 0
        down = True
        for char in text:
            matrix[row][col] = char
            col += 1
            if down:
                row += 1
                if row == rows - 1:
                    down = False
            else:
                row -= 1
                if row == 0:
                    down = True
        # Matrisi oku
        result = ""
        for row in matrix:
            result += ''.join(row)
        return result

    @staticmethod
    def vigenere_encrypt(text: str, key: str) -> str:
        """Vigenere şifreleme algoritması"""
        result = ""
        key = key.upper()
        key_index = 0
        for char in text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                key_char = key[key_index % len(key)]
                key_shift = ord(key_char) - ord('A')
                result += chr((ord(char) - ascii_offset + key_shift) % 26 + ascii_offset)
                key_index += 1
            else:
                result += char
        return result

    @staticmethod
    def four_square_encrypt(text: str, key1: str, key2: str) -> str:
        """4 Kare şifreleme algoritması"""
        # Alfabe matrislerini oluştur
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # J harfi çıkarıldı
        key1 = key1.upper().replace('J', 'I')
        key2 = key2.upper().replace('J', 'I')
        
        # Anahtar matrislerini oluştur
        def create_matrix(key):
            matrix = []
            used = set()
            # Anahtarı ekle
            for char in key:
                if char not in used:
                    matrix.append(char)
                    used.add(char)
            # Kalan harfleri ekle
            for char in alphabet:
                if char not in used:
                    matrix.append(char)
            return matrix
        
        matrix1 = create_matrix(key1)
        matrix2 = create_matrix(key2)
        
        # Metni çiftler halinde işle
        text = text.upper().replace('J', 'I')
        # Tek sayıda karakter varsa sona X ekle
        if len(text) % 2 != 0:
            text += 'X'
        
        result = ""
        for i in range(0, len(text), 2):
            char1, char2 = text[i], text[i+1]
            # İlk matriste konumları bul
            pos1 = matrix1.index(char1)
            pos2 = matrix2.index(char2)
            # Yeni karakterleri bul
            row1, col1 = divmod(pos1, 5)
            row2, col2 = divmod(pos2, 5)
            new_char1 = matrix1[row1 * 5 + col2]
            new_char2 = matrix2[row2 * 5 + col1]
            result += new_char1 + new_char2
        return result


    @staticmethod
    def hill_encrypt(text: str, key: List[List[int]]) -> str:
        """Hill şifreleme algoritması"""
        # Matris boyutunu kontrol et
        n = len(key)
        if n != len(key[0]):
            raise ValueError("Anahtar matrisi kare olmalıdır")
        
        # Metni büyük harfe çevir ve boşlukları kaldır
        text = text.upper()
        text = ''.join(text.split())
        
        # Eksik karakterleri doldur
        while len(text) % n != 0:
            text += 'X'
        
        # Metni sayısal vektörlere dönüştür
        vectors = []
        for i in range(0, len(text), n):
            vector = [ord(c) - ord('A') for c in text[i:i+n]]
            vectors.append(vector)
        
        # Matris çarpımı yap
        result = ""
        key_matrix = np.array(key)
        for vector in vectors:
            encrypted = np.dot(key_matrix, vector) % 26
            result += ''.join([chr(x + ord('A')) for x in encrypted])
        
        return result
    
    