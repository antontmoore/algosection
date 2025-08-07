from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(string):
            return string == string[::-1]

        output = []

        def dfs(cur_parts, idx):
            if idx == len(s):
                output.append(cur_parts)

            for i in range(idx + 1, len(s) + 1):
                if is_palindrome(s[idx:i]):
                    dfs(cur_parts + [s[idx:i]], i)

        dfs([], 0)
        return output


if __name__ == "__main__":
    s = Solution()
    res = s.partition("aab")
    print(res)
