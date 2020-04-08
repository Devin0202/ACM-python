# -*- coding: utf-8 -*-
import sys
import os
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def layer2BinaryTree(nums):
        nodesList = []
        for i in nums:
            if "null" == i:
                nodesList.append(None)
            else:
                nodesList.append(TreeNode(i))
        
        nodesCnt = len(nodesList)
        for i in range((nodesCnt + 1) // 2):
            l = 2 * i + 1
            r = l + 1
            if l < nodesCnt:
                nodesList[i].left = nodesList[l]
            else:
                pass
            if r < nodesCnt:
                nodesList[i].right = nodesList[r]
            else:
                pass
        
        return nodesList[0]

from typing import List
import re
from collections import Counter, deque
from itertools import combinations, permutations
from functools import reduce
import copy

class Solution:
    def dp(self):
        l = self.len
        self.palindromeDP = [[False for j in range(l)] for i in range(l)]
        for i in range(l):
            self.palindromeDP[i][i] = True
        for i in range(l - 1, -1, -1):
            for j in range(i + 1, l):
                if self.s[i] != self.s[j]:
                    pass
                else:
                    if j == i + 1:
                        self.palindromeDP[i][j] = True
                    elif True == self.palindromeDP[i + 1][j - 1]:
                        self.palindromeDP[i][j] = True
                    else:
                        pass
        return

    def dfs(self, start, trace):
        if start == self.len:
            self.rtv.append(trace)
        else:
            for i in range(start, self.len):
                if self.palindromeDP[start][i]:
                    self.dfs(i + 1, trace + [self.s[start:i + 1]])
                else:
                    continue
        return

    def partition(self, s: str) -> List[List[str]]:
        self.rtv = []
        self.s = s
        self.len = len(s)
        self.palindromeDP = []
        self.dp()
        self.dfs(0, [])
        return self.rtv


a = Solution()
b = a.partition("aab")
print(b)

