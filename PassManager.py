from cryptography.fernet import Fernet

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")




while True:

    print("Enter: 1 to View saved Passwords")
    print("Enter: 2 to add new Password")
    print("Enter: 0 to quit")
    mode = int(input())
    if mode == 0:
        break

    if mode == 1:
        view()
    elif mode == 2:
        add()
    else:
        print("Invalid Choice")
        continue
