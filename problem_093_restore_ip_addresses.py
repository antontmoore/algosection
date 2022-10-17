from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        def backtrack(cur_ip=[], num='', idx=0):
            if idx == len(s):
                if len(cur_ip) == 4 and len(num) == 0:
                    res.append('.'.join(cur_ip))
                return


            c = s[idx]
            new_value = num + c
            if int(new_value) > 255:
                return

            if new_value != '0':
                # add to current num
                backtrack(cur_ip, new_value, idx + 1)


            # start new num
            cur_ip.append(new_value)
            backtrack(cur_ip, '', idx + 1)
            cur_ip.pop()

        backtrack()

        return res


if __name__ == "__main__":
    s = Solution()
    st = '25525511135'
    st = '101023'
    print(s.restoreIpAddresses(st))




