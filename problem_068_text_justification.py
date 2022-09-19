from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lens = [len(word) for word in words]
        string_word_ids, string = [], []

        j = 0

        while j < len(words):
            # can we put it in string?
            if sum([lens[idx] for idx in string]) + len(string) + lens[j] <= maxWidth:
                string.append(j)
            else:
                string_word_ids.append(string)
                string = [j]
            j += 1

        last_string = string if len(string) > 0 else string_word_ids.pop()

        res = []
        for string in string_word_ids:
            if len(string) == 1:
                str_to_add = words[string[0]] + ' ' * (maxWidth - len(words[string[0]]))
            else:
                spaces_num = maxWidth - sum([lens[idx] for idx in string])
                gaps = len(string) - 1

                min_spaces = spaces_num // gaps
                lost_spaces = spaces_num % gaps

                str_to_add = ''
                for j, word_id in enumerate(string[:-1]):
                    str_to_add += words[word_id] + ' ' * min_spaces
                    if j < lost_spaces:
                        str_to_add += ' '
                str_to_add += words[string[-1]]
            res.append(str_to_add)

        str_to_add = ' '.join([words[idx] for idx in last_string])
        if len(str_to_add) > maxWidth:
            str_to_add = str_to_add[:-1]
        else:
            str_to_add += ' ' * (maxWidth - len(str_to_add))
        res.append(str_to_add)

        return res


if __name__ == "__main__":
    # words = ["This", "is", "an", "example", "of", "text", "justification."]
    # maxWidth = 16

    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth = 16
    s = Solution()
    print(s.fullJustify(words, maxWidth))