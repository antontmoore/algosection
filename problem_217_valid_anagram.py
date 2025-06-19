class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1

        for c in t:
            have_c = d.get(c, 0)
            have_c -= 1
            if have_c < 0:
                return False
            d[c] = have_c

        return sum(d.values()) == 0