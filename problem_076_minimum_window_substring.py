class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def idx(letter):
            return ord(letter) - ord('A')

        def is_substring(big_arr, small_arr):
            for j in range(len(big_arr)):
                if small_arr[j] > big_arr[j]:
                    return False
            return True

        total_number_of_letters = idx('z') - idx('A') + 1
        t_arr = [0 for _ in range(total_number_of_letters)]
        s_arr = [0 for _ in range(total_number_of_letters)]

        for c in t:
            t_arr[idx(c)] += 1

        need = sum([1 for l in t_arr if l > 0])
        have = 0
        min_length = 2 * len(s)
        best_window = ""
        l = 0
        for r in range(len(s)):
            c = s[r]
            s_arr[idx(c)] += 1

            if t_arr[idx(c)] == s_arr[idx(c)]:
                have += 1

            while have == need:
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    best_window = s[l: r + 1]

                s_arr[idx(s[l])] -= 1
                if t_arr[idx(s[l])] > s_arr[idx(s[l])]:
                    have -= 1
                l += 1

        return best_window


if __name__ == "__main__":
    s = Solution()

    # res = s.minWindow("ADOBECODEBANC", "ABC")
    # res = s.minWindow("aa", "aa")
    res = s.minWindow("cgklivwehljxrdzpfdqsapogwvjtvbzahjnsejwnuhmomlfsrvmrnczjzjevkdvroiluthhpqtffhlzyglrvorgnalk",
                      "mqfff")
    print(res)