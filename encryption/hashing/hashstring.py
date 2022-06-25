import _sha256 as s

def hash_string(str):
    return s.sha256(str.encode()).hexdigest()

def write_password(password):
    with open("encryption/hashing/passtext.txt", "w", encoding="utf-8") as f:
        f.writelines(password)

def run():
    start_password = input("Enter a password: ")
    hash_start = hash_string(start_password)

    confirm_password = input("Confirm the password: ")
    hash_confirm = hash_string(confirm_password)

    if hash_start == hash_confirm:
        print("Passwords match")
        write_password(hash_confirm)
    else:
        print("The passwords do not match.")

run()
