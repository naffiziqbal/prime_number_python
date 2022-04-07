def is_prime(n):
    if n < 2:
        return False
    prime = True
    #
    #
    if n == 2:
        return True
    for x in range(2,n):
        if n % x == 0:
            print(n,"Is Divisible by ", x)
            prime = False
            return prime
        return prime
while True:
    n1 = int(input("Enter: "))
    n2 = int(input("Enter: "))
    for number in range (n1, n2):
     if number == 0:
        break
    prime = is_prime(number)
    if prime is True:
        print(number, "Is a prime")

    else:
        print("False")
