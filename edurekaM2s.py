from cryptography.fernet import Fernet
import re

def generate_key():
    return Fernet.generate_key()
def encrypt_data(key, data):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode('utf-8'))
    return encrypted_data
def decrypt_data(key, encrypted_data):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode('utf-8')
    return decrypted_data
def validate_reference_id(reference_id):
    if not (8 <= len(reference_id) <= 20):
        return False
    if not re.match("^[a-zA-Z0-9@#$%^&+=]+$", reference_id):
        return False
    return True
def main():
    encryption_key = generate_key()
    reference_id = input("Enter Reference ID: ")
    if validate_reference_id(reference_id):
        encrypted_reference_id = encrypt_data(encryption_key, reference_id)
        print("Encrypted Reference ID:", encrypted_reference_id)
        decrypt_choice = input("Do you want to decrypt the Reference ID? (yes/no): ").lower()
        if decrypt_choice == "yes":
            decrypted_reference_id = decrypt_data(encryption_key, encrypted_reference_id)
            print("Decrypted Reference ID:", decrypted_reference_id)
    else:
        print("Reference ID is invalid. Please make sure it has 8 to 20 characters and contains only alphanumeric characters and some special characters.")
if __name__ == "__main__":
    main()
