def is_armstrong(number: int) -> bool:
    total = 0
    
    for digit in str(number):
        total = total + int(digit) ** len(str(number))

    if total == number:
        return True
    return False

if __name__ == '__main__':
    x = 1
    while True:
        if (is_armstrong(x)):
            print(x)
        x = x + 1