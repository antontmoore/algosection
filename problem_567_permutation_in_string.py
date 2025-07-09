class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if len(s1) == 0:
            return True
        if len(s1) == 1 and s1[0] in s2:
            return True

        s1arr = [0 for _ in range(26)]
        s2arr = [0 for _ in range(26)]

        for j in range(len(s1)):
            s1arr[ord(s1[j]) - ord('a')] += 1
            s2arr[ord(s2[j]) - ord('a')] += 1

        for i in range(len(s2) - len(s1)):
            if s1arr == s2arr:
                return True
            s2arr[ord(s2[i]) - ord('a')] -= 1
            s2arr[ord(s2[i + len(s1)]) - ord('a')] += 1

        return s1arr == s2arr


