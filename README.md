# Palindrome-discovery
Python code for solving palindrome

Code generates an array of strings and put them in three different palindrome functions.
The strings are either palindrome or completely not.

The first function is the normal O(n) function.
The other two functions contain hash functions instead of regular checks.

As the length of the strings increases, the regular O(n) method sees significant increase in execution time.

```
palnum: 4928/10000
stringlength: 10000
regular: 7.592935199999999 4928
palhash1: 0.7576461999999964 4928
palhash2: 0.39290870000000666 4928

palnum: 5024/10000
stringlength: 1000
regular: 0.7664700999999994 5024
palhash1: 0.08264349999999965 5024
palhash2: 0.052620199999999784 5024

palnum: 4999/10000
stringlength: 100
regular: 0.06728960000000006 4999
palhash1: 0.01427400000000012 4999
palhash2: 0.015370099999999942 4999

palnum: 4985/10000
stringlength: 10
regular: 0.014949099999999937 4985
palhash1: 0.007752699999999946 4985
palhash2: 0.011713399999999985 4985
```

Hardware:
CPU: Ryzen5 1600
RAM: 16G 2400 MHz single slot
