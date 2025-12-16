n = int(input().strip())

if n % 2 != 0:
    print("Weird")
else:
    # n is even
    if n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    else:
        # n is greater than 20
        print("Not Weird")
