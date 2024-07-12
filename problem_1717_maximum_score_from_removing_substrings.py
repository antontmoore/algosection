class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        s = [c for c in s]

        def collapse(pattern, score):
            nonlocal s
            points = 0
            stack = []
            for c in s:
                if c == pattern[1] and stack and stack[-1] == pattern[0]:
                    stack.pop()
                    points += score
                else:
                    stack.append(c)
            s = "".join(stack)
            return points

        pattern = 'ab' if x > y else 'ba'
        total_points = collapse(pattern, max(x, y))
        total_points += collapse(pattern[::-1], min(x, y))
        return total_points


if __name__ == "__main__":
    s = Solution()
    print(s.maximumGain('cdbcbbaaabab', 4, 5))