import os
from cryptography.fernet import Fernet

VAULT_FILE = "secure_vault.dat"

def load_vault_key():
    key_file = "vault.key"
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, "wb") as f:
            f.write(key)
    else:
        key = open(key_file, "rb").read()
    return key

def get_vault():
    key = load_vault_key()
    f = Fernet(key)

    if not os.path.exists(VAULT_FILE):
        default = b"{}"
        with open(VAULT_FILE, "wb") as f_out:
            f_out.write(f.encrypt(default))

    encrypted = open(VAULT_FILE, "rb").read()
    decrypted = f.decrypt(encrypted)
    return eval(decrypted)

def save_vault(data: dict):
    key = load_vault_key()
    f = Fernet(key)
    encrypted = f.encrypt(str(data).encode())

    with open(VAULT_FILE, "wb") as f_out:
        f_out.write(encrypted)
