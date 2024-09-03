from cryptography.fernet import Fernet
import hashlib

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_master_password(input_password):
    stored_hash = open("master_password.hash", "r").read()
    return hash_password(input_password) == stored_hash

def setup_master_password():
    master_pwd = input("Set your master password: ")
    with open("master_password.hash", "w") as f:
        f.write(hash_password(master_pwd))
    print("Master password set.")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" in data: 
                user, passw = data.split("|")
                print("User:", user, "Password:", fer.decrypt(passw.encode()).decode() + "\n")
            else:
                print("Skipping malformed line:", data)

def add():
    name = input('Account name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")



if __name__ == "__main__":
    
    try:
        open("master_password.hash", "r")
    except FileNotFoundError:
        setup_master_password()

    master_pwd = input("Enter the master password: ")

    if not verify_master_password(master_pwd):
        print("Invalid master password!")
        exit()

    key = load_key()
    fer = Fernet(key)

    while True:
        mode = input("Would you like to add a new password or view the existing passwords (view, add), press q to quit: ").lower()
        if mode == "q":
            break

        if mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid mode.")
            continue
