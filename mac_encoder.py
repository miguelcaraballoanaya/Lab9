def encode(password):
    encoded_password = ""
    for char in password:
        if char == "1":
            encoded_password += "4"
        elif char == "2":
            encoded_password += "5"
        elif char == "3":
            encoded_password += "6"
        elif char == "4":
            encoded_password += "7"
        elif char == "5":
            encoded_password += "8"
        elif char == "6":
            encoded_password += "9"
        elif char == "7":
            encoded_password += "0"
        elif char == "8":
            encoded_password += "1"
        elif char == "9":
            encoded_password += "2"
        elif char == "0":
            encoded_password += "3"
    return encoded_password


def main():
    choice = 0
    while choice != 3:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = str(input("Please nter the password to encode: "))
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif choice == 2:
            # decoded_password = decode(password)
            # print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            pass
        elif choice == 3:
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()