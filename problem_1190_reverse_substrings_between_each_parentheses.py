class Solution:
    def reverseParentheses(self, s: str) -> str:
        opening = []
        s = list([c for c in s])
        for j, c in enumerate(s):
            if c == '(':
                opening.append(j)
            elif c == ')':
                start = opening.pop()
                s[start + 1: j] = s[j-1: start:-1]

        return ''.join([c for c in s if c != '(' and c != ')'])


if __name__ == "__main__":
    s = Solution()
    print(s.reverseParentheses('(ed(et(oc))el)'))