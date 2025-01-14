'''
IDK abt the inputs rn
'''
import os

def generate_hist(filename) -> list:
    cwd = os.getcwd()
    print(cwd)
    cwd += "/" + filename
    result = [0 for x in range(26)]
    with open(cwd, "r") as file:
        for line in file:
            for character in line:
                if(character == '\n'):
                    break
                result[ord(character) - 65] += 1

    return result

if __name__ == "__main__":
    result = generate_hist("test.txt")
    for i in range(len(result)):
        print(chr(i + 65) + ": " + str(result[i]))
