class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        # parts = list(filter(lambda x: x != '/', parts))
        res = []
        for p in parts:
            if p == "." or p == "":
                continue
            elif p == "..":
                if len(res) > 0:
                    res.pop()
            else:
                res.append(p)

        return "/" + '/'.join(res)




if __name__ == "__main__":
    path = "/home/../foo/"
    path = "/.../"

    s = Solution()
    ans = s.simplifyPath(path)
    print(ans)

