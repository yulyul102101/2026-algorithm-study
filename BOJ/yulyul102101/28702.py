import sys 

def fizzbuzz(n: int):
    if n % 3 == 0 and n % 5 == 0:
        return("FizzBuzz")
    elif n % 3 == 0:
        return("Fizz")
    elif n % 5 == 0:
        return("Buzz")
    else:
        return(n)
        

strings = [str(sys.stdin.readline().strip()) for _ in range(3)]
arr = [1, 2]

if strings[0].isdigit():
    n = int(strings[0]) + 3
    print(fizzbuzz(n))
elif strings[1].isdigit():
    n = int(strings[1]) + 2
    print(fizzbuzz(n))
elif strings[2].isdigit():
    n = int(strings[2]) + 1
    print(fizzbuzz(n))
else:
    for i in range(2, 1000000):
        arr.append(fizzbuzz(i))
        if arr[i-2:] == strings:
            print(fizzbuzz(i + 1))
            break