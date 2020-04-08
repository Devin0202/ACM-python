# -*- coding: utf-8 -*-
import sys
import os
import math

from typing import List
import re
from collections import Counter, deque
from itertools import combinations, permutations
from functools import reduce
import copy

class Solution:
    """
    Find all Palindromes in a string.
    It will return a 2-D bool array, like "palindromeDP[i][j]"
    "i" means start index in the given string and "j" means end index,
    the value "palindromeDP[i][j]" means that if this sub is a palindrome.
    """
    def subPalindromes(self, str):
        l = len(str)
        self.palindromeDP = [[False for j in range(l)] for i in range(l)]
        for i in range(l):
            self.palindromeDP[i][i] = True
        for i in range(l - 1, -1, -1):
            for j in range(i + 1, l):
                if str[i] != str[j]:
                    pass
                else:
                    if j == i + 1:
                        self.palindromeDP[i][j] = True
                    elif True == self.palindromeDP[i + 1][j - 1]:
                        self.palindromeDP[i][j] = True
                    else:
                        pass
        return self.palindromeDP

a = Solution()
b = a.subPalindromes("aab")
print(b)

