class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"CM": 900, "M": 1000, "CD": 400, "D": 500,
             "XC": 90, "C": 100, "XL": 40, "L": 50,
             "IX": 9, "X": 10, "IV": 4, "V": 5, "I": 1}

        ans = 0
        j = 0
        while j < len(s):
            for key in d.keys():
                if j + len(key) <= len(s) and s[j: j + len(key)] == key:
                    ans += d[key]
                    j += len(key)
                    break
        return ans