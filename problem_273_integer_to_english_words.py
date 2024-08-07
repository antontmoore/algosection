class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        def helper(n):
            digit_to_word = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
                             9: 'Nine'}
            tens_to_word = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty',
                            9: 'Ninety'}
            teen_to_word = {0: 'Ten', 1: 'Eleven', 2: 'Twelve', 3: 'Thirteen', 4: 'Fourteen', 5: 'Fifteen',
                            6: 'Sixteen', 7: 'Seventeen', 8: 'Eighteen', 9: 'Nineteen'}
            hundreds = n // 100
            n %= 100
            tens = n // 10
            ones = n % 10

            words = []
            if hundreds != 0:
                words.extend([digit_to_word[hundreds], 'Hundred'])

            if tens == 0:
                if ones > 0:
                    words.append(digit_to_word[ones])
            elif tens == 1:
                words.append(teen_to_word[ones])
            else:
                words.append(tens_to_word[tens])
                if ones != 0:
                    words.append(digit_to_word[ones])

            return ' '.join(words)

        blocks = []
        block_names = ['Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion']
        j = 0
        while num != 0:
            block = helper(num % 1000)
            if len(block) > 0:
                if j > 0 and j < 5:
                    blocks.append(block_names[j - 1])

                blocks.append(block)
            num //= 1000
            j += 1

        return ' '.join(blocks[::-1])


if __name__ == "__main__":
    s = Solution()
    res = s.numberToWords(1000000)
    print(res)