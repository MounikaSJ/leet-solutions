class Solution:
    def reverseString(self, s: List[str]) -> None:
        L = 0
        R = len(s) - 1

        while L < R:
            extra = s[R]
            s[R] = s[L]
            s[L] = extra

            L += 1
            R -= 1