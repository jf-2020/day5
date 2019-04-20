# fib.py - computes nth fibonacci number
#
# jf - 4/19


def fib_n(n):
    # computes the nth fibonacci number

    a, b = 1, 1
    
    if n == 0 or n == 1:
        return a
    
    else:
        
        for _ in range(2,n):
        
            a, b = b, a+b
        
        return b


def solves_the_problem():
    # computes the sum of the fibonacci numbers that're both even and
    # less than or equal to 4,000,000

    print("inside the function")

    MAX = 4 * (10**6)
    count = 0
    running_sum = 0

    while running_sum <= MAX:
        
        fib = fib_n(count)

        if fib % 2 == 0:
            print("running sum: %d" % running_sum)
            running_sum += fib

        print("count: %d" % count)
        count += 1

    return running_sum
    

def main():
    # main function associated with fibonacci problem
    
    # tests = [i for i in range(1, 10)]
    # for test in tests:
    #     print("Computing %dth fib number: %d" % (test, fib_n(test)))

    print("The answer is: %d" % solves_the_problem())


# to be run as script
if __name__ == "__main__":
    main()