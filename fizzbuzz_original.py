def fizzbuzz(n):
    for i in range(n):
        print_str = ''
        if i % 3 == 0:
            print_str += 'Fizz'
        if i % 5 == 0:
            print_str += 'Buzz'
        if not print_str:
            print_str = i
        print(print_str)


if __name__ == "__main__":
    fizzbuzz(int(input("Enter a number: ")))
