class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for i in range(len(digits) - 1, -1, -1):
            number += 10**i * digits[len(digits)-i-1]
        number += 1
        number = str(number)
        return [int(i) for i in number]