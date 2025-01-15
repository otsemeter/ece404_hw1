'''
again idk abt inputs
'''


def encrypt(key, message) -> str:
    i = 0
    message = message.upper()
    key = key.upper()
    result = ""
    for x in range(len(message)):
        result += chr((ord(message[x]) - 65 + ord(key[i]) - 65) % 26 + 65)
        i += 1
        if i == len(key):
            i = 0

    return result


if __name__ == "__main__":
    key = input("input encryption key: ")
    message = input("input message: ")
    encrypted = encrypt(key, message)
    print(encrypted)
