def encrypt(text, shift):
    encrypted = ""

    for char in text:

        if char.isalpha():

            if char.isupper():
                encrypted += chr((ord(char) - 65 + shift) % 26 + 65)

            else:
                encrypted += chr((ord(char) - 97 + shift) % 26 + 97)

        else:
            encrypted += char

    return encrypted


def decrypt(text, shift):
    decrypted = ""

    for char in text:

        if char.isalpha():

            if char.isupper():
                decrypted += chr((ord(char) - 65 - shift) % 26 + 65)

            else:
                decrypted += chr((ord(char) - 97 - shift) % 26 + 97)

        else:
            decrypted += char

    return decrypted


def main():

    print("=" * 50)
    print(" Basic Encryption & Decryption (Caesar Cipher)")
    print("=" * 50)

    text = input("\nEnter Your Text : ")

    shift = int(input("Enter Shift Key (1-25): "))

    encrypted_text = encrypt(text, shift)

    decrypted_text = decrypt(encrypted_text, shift)

    print("\n----------- RESULT -----------")
    print("Original Text  :", text)
    print("Encrypted Text :", encrypted_text)
    print("Decrypted Text :", decrypted_text)
    print("------------------------------")


if __name__ == "__main__":
    main()

from encrypt import encrypt
from decrypt import decrypt
from utils import get_shift


def banner():

    print("=" * 60)
    print("      BASIC ENCRYPTION & DECRYPTION")
    print("          Caesar Cipher Project")
    print("=" * 60)


def menu():

    print("\n1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Exit")


while True:

    banner()

    menu()

    choice = input("\nChoose Option : ")

    if choice == "1":

        text = input("\nEnter Text : ")

        shift = get_shift()

        encrypted = encrypt(text, shift)

        print("\nEncrypted Text")
        print("----------------------")
        print(encrypted)

    elif choice == "2":

        text = input("\nEnter Encrypted Text : ")

        shift = get_shift()

        decrypted = decrypt(text, shift)

        print("\nDecrypted Text")
        print("----------------------")
        print(decrypted)

    elif choice == "3":

        print("\nThank you for using the program.")

        break

    else:

        print("\nInvalid Option.")