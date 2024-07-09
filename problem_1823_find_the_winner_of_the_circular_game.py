class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [j + 1 for j in range(n)]
        pointer = 0
        while len(friends) > 1:
            to_del = (pointer + k - 1) % len(friends)
            pointer = (to_del) % len(friends)
            friends.pop(to_del)
        return friends[0]

if __name__ == "__main__":
    s = Solution()
    res = s.findTheWinner(5, 2)
    print(res)