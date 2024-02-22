def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def run():
    with open("./names.txt", "r", encoding="utf-8") as f: 
        names = [linea.rstrip('\n') for linea in f]

    print(names)
    
    for linea in names:
        if is_palindrome(linea):
            print(linea + " es palindromo")    

if __name__ == '__main__':
    run()

