import mylib.mat

def main():
    obj = mylib.mat.MyClass()
    a, b = 3, 5
    result = obj.Sum(a, b)
    print(a, '+', b, '=', result)
    result = obj.WrongSum(a, b)
    print(a, '+', b, '=', result)

if __name__ == '__main__':
    main()
