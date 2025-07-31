class TimeMap:

    def __init__(self):
        self.store = dict()  # key = key, value = [list_of_ts, list_of_vals]

    def set(self, key: str, value: str, timestamp: int) -> None:
        val = self.store.get(key, [[], []])
        val[0].append(timestamp)
        val[1].append(value)
        self.store[key] = val

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        ts, vals = self.store[key]
        if timestamp < ts[0]:
            return ""

        left, right = 0, len(ts) - 1
        while left <= right:
            mid = (left + right) // 2
            if ts[mid] <= timestamp:
                if mid < len(ts) - 1 and ts[mid + 1] > timestamp:
                    return vals[mid]
                elif mid == len(ts) - 1:
                    return vals[mid]
                else:
                    left = mid + 1
            else:
                right = mid


if __name__ == "__main__":
    commands = ["TimeMap", "set", "set", "set", "get", "get", "get"]
    params = [[],["foo","bar",5],["foo","bar2",10],["foo","bar3",14],["foo",4],["foo",6],["foo",11]]

    for j in range(len(commands)):
        if commands[j] == "TimeMap":
            obj = TimeMap()
        elif commands[j] == "set":
            obj.set(params[j][0], params[j][1], params[j][2])
        else:
            res = obj.get(params[j][0], params[j][1])
            print(res)




# [[],["foo","bar",5],["foo","bar2",10],["foo","bar3",14],["foo",4],["foo",6],["foo",11]]