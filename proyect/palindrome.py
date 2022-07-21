def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def run():
    word: str = input("Get a word: ")

    print(word + ' ' + str(is_palindrome(word)) )

if __name__ == '__main__':
    run()

