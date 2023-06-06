import hashlib

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# باز کردن فایل و خواندن پسوردها
with open("hash.txt", "r") as file:
    passwords = file.readlines()

# هش کردن پسوردها و ذخیره در دیکشنری
hashed_passwords = {}
for password in passwords:
    hashed_password = hash_password(password.strip())
    hashed_passwords[password.strip()] = hashed_password

# نوشتن دیکشنری در فایل txt
with open("hashed_passwords.txt", "w") as file:
    for password, hashed_password in hashed_passwords.items():
        file.write(f"Password: {password}, Hashed Password: {hashed_password}\n")


