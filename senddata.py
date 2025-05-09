import encryption as enc
import socket
import pickle

def send_encrypted_message(choice, encrypted_text, key):
    """Şifreli metni sunucuya gönderir"""
    SERVER_IP = '127.0.0.1' # Buraya alıcı sunucunun IP adresini yazılacak
    PORT = 12345 # Rastgele bir port numarası seçildi

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        client.connect((SERVER_IP, PORT))
        payload = (choice, encrypted_text, key)
        client.sendall(pickle.dumps(payload))
        client.close()
    except Exception as e:
        print(f"Gönderme sırasında hata oluştu: {e}")