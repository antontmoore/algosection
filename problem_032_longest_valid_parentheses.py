class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for j, c in enumerate(s):
            if c == '(':
                stack.append(j)
            else:
                stack.pop()
                if not stack:
                    stack.append(j)
                else:
                    cur_len = j - stack[-1]
                    max_len = max(max_len, cur_len)

        return max_len


if __name__ == "__main__":
    s = Solution()
    res = s.longestValidParentheses("))))()())")
    print(res)