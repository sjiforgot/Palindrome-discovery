#!/usr/bin/env python3

import string
import random
import time

class palindrome_solver:
    palnum = 0
    stringlength = 1000

    def palindrome(self, length):
        s = ''.join(random.choice(string.ascii_lowercase) for i in range(length//2))
        self.palnum += 1
        return s + s[::-1]

    def not_palindrome(self, length):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

    def generate(self, length):
        if int(random.choice(string.digits)) > 4:
            return self.not_palindrome(length)
        return self.palindrome(length)

    def palnormal(self, string):
        for i in range(len(string) // 2):
            if string[i] != string[len(string) - i - 1]:
                return False
        return True

    # use hash for the complete string
    def palhash1(self, string):
        return hash(string) == hash(string[::-1])

    # use hash to check half of the string
    def palhash2(self, string):
        return hash(string[:len(string)//2]) == hash(string[:len(string)//2-1:-1])

    def __init__(self, stringlength):
        memory = [self.generate(stringlength) for i in range(10000)]
        print("palnum: {}/{}\nstringlength: {}".format(self.palnum, len(memory), stringlength))

        counter = 0
        starttime = time.perf_counter()
        for i in memory:
            if self.palnormal(i):
                counter += 1
        endtime = time.perf_counter()

        print("regular: {} {}".format(endtime - starttime, counter))

        counter = 0
        starttime = time.perf_counter()
        for i in memory:
            if self.palhash1(i):
                counter += 1
        endtime = time.perf_counter()

        print("palhash1: {} {}".format(endtime - starttime, counter))

        counter = 0
        starttime = time.perf_counter()
        for i in memory:
            if self.palhash2(i):
                counter += 1
        endtime = time.perf_counter()

        print("palhash2: {} {}".format(endtime - starttime, counter))
        return

palindrome_solver(1000)
