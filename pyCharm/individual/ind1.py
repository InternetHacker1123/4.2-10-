#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Pair:
    def __init__(self, first, second):
        if not isinstance(first, int) or not isinstance(second, int):
            raise ValueError("Both values should be integers")
        self.first = first
        self.second = second

    def read(self):
        self.first = int(input("Enter the first number: "))
        self.second = int(input("Enter the second number: "))

    def display(self):
        print(f"Pair: ({self.first}, {self.second})")

    def __str__(self):
        return f"Pair: ({self.first}, {self.second})"

    def __lt__(self, other):
        return self.first < other

    def __le__(self, other):
        return self.first <= other

    def __gt__(self, other):
        return self.first > other

    def __ge__(self, other):
        return self.first >= other

    def __eq__(self, other):
        return self.first == other

    def __ne__(self, other):
        return self.first != other


if __name__ == "__main__":
    # Пример использования класса Pair
    pair = Pair(1, 5)
    print(pair)

    num = int(input("Enter a number to check against the range: "))
    if num in pair:
        print(f"{num} is in the range [{pair.first}, {pair.second})")
    else:
        print(f"{num} is not in the range [{pair.first}, {pair.second})")
