def fibonacci_generator(n):

    fib_sequence = [0, 1]


    for i in range(2, n):

        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence

n = int (input("Enter the number : "))


if n < 0:
    print("Please enter a positive integer.")
elif n == 0:
    print("fibonacci number of " ,n, "is ['0']")
elif n == 1:
    print("fibonacci number of " ,n, "is ['1'] ")
else:
    result = fibonacci_generator(n)
    print("fibonacci number of " ,n, "is ", result)
