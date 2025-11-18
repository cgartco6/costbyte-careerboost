import bcrypt
import hashlib
import os

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

def military_grade_security():
    os.system("ufw default deny incoming")
    os.system("ufw allow 443")
    os.system("ufw allow 80")
    os.system("ufw enable")
