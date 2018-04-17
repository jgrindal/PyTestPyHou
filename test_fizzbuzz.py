import pytest
from fizzbuzz import fizzbuzz_list


def test_make_fizzbuzz_list():
    expected_list = ['1',
                     '2',
                     'Fizz',
                     '4',
                     'Buzz',
                     'Fizz',
                     '7',
                     '8',
                     'Fizz',
                     'Buzz',
                     '11',
                     'Fizz',
                     '13',
                     '14',
                     'FizzBuzz',
                     '16',
                     '17',
                     'Fizz',
                     '19',
                     'Buzz']

    test_list = fizzbuzz_list(20)
    assert test_list == expected_list


def test_fizzbuzz_exception():
    with pytest.raises(TypeError):
        fizzbuzz_list('a')