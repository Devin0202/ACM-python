# coding: utf-8
import sys
import collections

class Solution:
    def kmpCreate(self, patternS):
        rtv = []
        L = len(patternS)
        if 0 == L:
            pass
        else:
            for i in range(L):
                if 0 == i:
                    rtv.append(0)
                elif 1 == i:
                    rtv.append(0)
                else:
                    j = 1
                    while j < i:
                        if patternS[j - 1] == patternS[i - j]:
                            j += 1
                        else:
                            break
                    rtv.append(j - 1)
        return rtv

    def kmp(self, patternS, mainS):
        maps = self.kmpCreate(patternS)
        st, search = 0, 0
        while st <= len(mainS) - len(patternS):
            if search == len(patternS):
                return True

            if mainS[st + search] == patternS[search]:
                search += 1
            else:
                if 0 == search:
                    st += 1
                    search = 0
                else:
                    sl = maps[search]
                    st = st + search -sl
                    search = sl
        return False