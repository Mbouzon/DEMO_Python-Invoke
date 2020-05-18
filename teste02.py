def teste():
    return "TESTE02"

def mathsum(num1, num2):
    result = 0
    if num1 > 0 and num2 > 0:
        result = num1 + num2
    return result

def main():
    print(mathsum(1,2))

if __name__ == "__main__":
    main()