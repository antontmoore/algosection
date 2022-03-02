from problem_004_median_of_two_sorted_arrays import Solution


tests = [{"a": [1, 2, 3, 4], "b": [5], "ans": 3},
         {"a": [2], "b": [], "ans": 2},
         {"a": [1, 7], "b": [9, 10, 15], "ans": 9},
         {"a": [2], "b": [], "ans": 2},
         {"a": [], "b": [9, 10, 15], "ans": 10},
         {"a": [1, 3], "b": [2], "ans": 2.0},
         {"a": [1, 2], "b": [3, 4], "ans": 2.5},
         {"a": [1, 3, 7], "b": [2, 5], "ans": 3},
         {"a": [1, 7], "b": [9, 10, 15], "ans": 9},
         ]

s = Solution()
for test in tests:
    # try:
    calc_ans = s.findMedianSortedArrays(test["a"], test["b"])
    right_ans = test["ans"]
    print(f" right: {right_ans}, calc: {calc_ans} ")
    # except IndexError:
    #     print("Index Error ---")




