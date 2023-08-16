from cryptography.fernet import Fernet
import os

def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key

def encrypt_master_password(key, master_pwd):
    fernet = Fernet(key)
    encrypted_master_pwd = fernet.encrypt(master_pwd.encode())
    with open("master_password.txt", "wb") as file:
        file.write(encrypted_master_pwd)

def decrypt_master_password(key):
    if os.path.exists("master_password.txt"):
        with open("master_password.txt", "rb") as file:
            encrypted_master_pwd = file.read()
            fernet = Fernet(key)
            master_pwd = fernet.decrypt(encrypted_master_pwd).decode()
            return master_pwd
    else:
        return None

def add():
    name = input('Account Name : ')
    pwd = input('password: ')

    with open('passwords.txt', 'a') as file:
        encrypted_pwd = fer.encrypt(pwd.encode()).decode()
        file.write(f"{name}|{encrypted_pwd}\n")

def view():
    view_master_pwd = input("Enter your master password to view passwords: ")

    if view_master_pwd == master_pwd:
        with open('passwords.txt', 'r') as file:
            for line in file:
                user, encrypted_passw = line.strip().split("|")
                decrypted_pwd = fer.decrypt(encrypted_passw.encode()).decode()
                print(f"User: {user}\nPassword: {decrypted_pwd}")
    else:
        print("Invalid master password. Access denied!")

key = load_key()
master_pwd = decrypt_master_password(key)

if not master_pwd:
    master_pwd = input("Please set your master password: ")
    encrypt_master_password(key, master_pwd)

fer = Fernet(key)

while True:
    mode = input("Would you like to add or view passwords? (view, add) : ")

    if mode in ["q", "quit", "exit"]:
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")