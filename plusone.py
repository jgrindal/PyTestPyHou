import pytest


def plusone(x):
    return x + 1


def test_plusone():
    assert plusone(3) == 5
