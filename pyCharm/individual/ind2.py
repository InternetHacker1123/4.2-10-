#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Money:
    def __init__(self, initial_data, max_size):
        self.data = initial_data
        self.size = max_size
        self.count = len(initial_data)

    def size(self):
        return self.size

    def __getitem__(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")
        return self.data[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        if index < self.count:
            self.data[index] = value
        else:
            self.data.append(value)
            self.count += 1


if __name__ == "__main__":
    initial_data = [{"10": 5}, {"20": 10}, {"50": 3}]
    max_size = 5
    money = Money(initial_data, max_size)

    print(money[0])  # Получить первый элемент
    print(money.size())  # Вывести установленный размер списка

    money[1] = {"100": 2}  # Установить новый элемент
    print(money[1])  # Получить обновленный элемент
    print(money.size())  # Вывести обновленный размер списка
