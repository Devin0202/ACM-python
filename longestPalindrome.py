# -*- coding: utf-8 -*-
import sys
import os
import math

from typing import List
import re
from collections import Counter
from itertools import combinations, permutations
from functools import reduce

class Solution:
    """Manacher algorithm for "longestPalindrome" is a dp solution"""
    def longestPalindrome(self, s: str) -> str:
        caret = '*'
        s = list(s)
        sLen = len(s)

        """Insert caret for uniting even and odd conditions"""
        sEx = [s[i // 2] if 1 == i & 1 else caret for i in range(2 * sLen + 1)]
        """Initializing "max length palindrome" array (lp) with index"""
        lp = [1 for i in sEx]
        """
        center -- center of current used palindrome
        current -- the index in lp array to calculate "max length palindrome"
        right -- (most) right boundary of current used palindrome
        radius -- variable for calculation
        """
        center, current, right = 0, 1, 0
        radius = None

        """Make out lp array"""
        while current < len(sEx):
            if current > right:
                """Naive way for finding palindrome when current beyond right"""
                for i in range(sLen + 1):
                    if 0 <= current - i and 2 * sLen >= current + i \
                        and sEx[current - i] == sEx[current + i]:
                        radius = i
                    else:
                        break
                lp[current] = 1 + 2 * radius
                right = current + radius
                center = current
            else:
                leftMirrorPoint = 2 * center - current
                leftRadius = (lp[leftMirrorPoint] - 1) // 2

                if right > current + leftRadius:
                    lp[current] = lp[leftMirrorPoint]
                elif right < current + leftRadius:
                    lp[current] = 1 + 2 * (right - current)
                    center = current
                else:
                    """
                    In "right == current + leftRadius" case, we wanna find that 
                    if the palindrome of "current" index can be extended
                    """
                    for i in range(leftRadius, sLen + 1):
                        if 0 <= current - i and 2 * sLen >= current + i \
                            and sEx[current - i] == sEx[current + i]:
                            radius = i
                        else:
                            break
                    lp[current] = 1 + 2 * radius
                    right = current + radius
                    center = current

            current += 1

        """Use lp and sEx to find first longestPalindrome"""
        mx = 0
        rtv = []
        for i in range(len(lp)):
            if mx > lp[i] or (caret == sEx[i] and 1 == lp[i]):
                continue
            elif mx < lp[i]:
                mx = lp[i]
                radius = (mx - 1) // 2
                tmp = sEx[i - radius:i + radius]
                tmp = "".join(tmp)
                tmp = tmp.replace(caret, '')
                rtv = [tmp]
            else:
                radius = (mx - 1) // 2
                tmp = sEx[i - radius:i + radius]
                tmp = "".join(tmp)
                tmp = tmp.replace(caret, '')
                rtv.append(tmp)

        return "" if [] == rtv else rtv[0]

a = Solution()
b = a.longestPalindrome("cbbd")
print(b)