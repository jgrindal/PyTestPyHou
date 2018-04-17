def fizzbuzz_list(n):
    """Performs fizzbuzz operation and returns a list of strings"""
    if not isinstance(n, int):
        raise TypeError
    fizzbuzz_list = []
    for i in range(1, n + 1):
        current_value = ''
        if i % 3 == 0:
            current_value += 'Fizz'
        if i % 5 == 0:
            current_value += 'Buzz'
        if not current_value:
            current_value = i
        fizzbuzz_list.append(current_value)
    return fizzbuzz_list


def print_list(to_print):
    """Prints all elements of a list"""
    for item in to_print:
        print(item)


def get_user_input():
    """Gets user input and returns it as an int"""
    n = int(input("Enter a Number to FizzBuzz: "))
    return n


if __name__ == "__main__":
    num = get_user_input()
    fizzbuzz = fizzbuzz_list(num)
    print_list(fizzbuzz)
