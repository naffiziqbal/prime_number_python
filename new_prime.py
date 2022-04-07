n1 = int(input("Enter any Number: "))
n2 = int(input("Enter any Number but bigger: "))
print("The Prime Numbers in range are: ")

for x in range(n1, n2 + 1):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                break
        else:
            print(x)
