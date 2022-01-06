#!/usr/bin/env python3

import string
import random
import time

class palindrome_by_1_solver:
    palnum = 0

    def palindrome(self, length):
        s = ''.join(random.choice(string.ascii_lowercase) for i in range(length//2))
        self.palnum += 1
        return s + s[::-1]

    def generate(self, length):
        s = self.palindrome(length)
        location = random.randrange(length//2)
        self.palnum += location
        temp = str(s[location]).upper()
        return s[:location] + temp + s[location+1:]

    def palslow(self, string):
        for i in range(len(string) // 2):
            if string[i] != string[len(string) - i - 1]:
                return i + 1
        return 0

    def palfast(self, string):
        start = 0
        end = len(string) // 2
        while end - start > 1:
            mid = end - (end - start) // 2
            if string[start:mid] == string[len(string)-start-1:len(string)-mid-1:-1]:
                start = mid
            else:
                end = mid
        return start + 1
                

    # use hash for the strings
    def palhash(self, string):
        start = 0
        end = len(string) // 2
        while end - start > 1:
            mid = end - (end - start) // 2
            if hash(string[start:mid]) == hash(string[len(string)-start-1:len(string)-mid-1:-1]):
                start = mid
            else:
                end = mid
        return start + 1

    def __init__(self, stringlength):
        self.palnum = 0
        memory = [self.generate(stringlength) for i in range(10000)]
        print("slow operations: {}\nstringlength: {}".format(self.palnum, stringlength))

        counter = 0
        starttime = time.perf_counter()
        for i in memory:
            counter += self.palslow(i)
        endtime = time.perf_counter()

        print("slow: {} {}".format(endtime - starttime, counter))

        counter = 0
        starttime = time.perf_counter()
        for i in memory:
            counter += self.palfast(i)
        endtime = time.perf_counter()

        print("fast: {} {}".format(endtime - starttime, counter))

        counter = 0
        starttime = time.perf_counter()
        for i in memory:
            counter += self.palhash(i)
        endtime = time.perf_counter()

        print("hash: {} {}".format(endtime - starttime, counter))
        return

palindrome_by_1_solver(10000)
