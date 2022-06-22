import _sha256 as s

def hash_string(str):
    return s.sha256(str.encode()).hexdigest()

def run():
    start_password = input("Enter a password: ")
    hash_start = hash_string(start_password)

    confirm_password = input("Confirm the password: ")
    hash_confirm = hash_string(confirm_password)

    if start_password == confirm_password:
        print("Passwords match")
    else:
        print("The passwords do not match.")

run()
