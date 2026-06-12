import random
import string
def generate_password():
    print("---secure password generator---")
    try:
        length=int(input("Enter the password length (eg.12):"))
    except ValueError:
        print("Enter a valid number")
        return

    all_characters=string.ascii_letters+string.digits+string.punctuation
    password=' '.join(random.choice(all_characters) for i in range(length))

    print(f"\nyour generated password is:{password}")

if __name__=="__main__":
    generate_password()