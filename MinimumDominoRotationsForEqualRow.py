class Solution:
    def minDominoRotations(self, T, B):
        return next((
            len(T) - max(T.count(x), B.count(x))
            for x in (T[0], B[0])
            if all(x in d for d in zip(T, B))), -1)
