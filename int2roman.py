class Solution:
    elementary = {
        1: 'I', 5: 'V', 10: 'X', 50: 'L',
        100: 'C', 500: 'D', 1000: 'M'
    }

    def get_interval(self, d: int) -> tuple:
        nums = sorted(list(self.elementary.keys()))
        for i, elt in enumerate(nums):
            lo = elt
            if lo <= d:
                if i == len(nums)-1:
                    hi = float('inf')
                else:
                    hi = nums[i+1]
                if d < hi:
                    return lo, hi

    def intToRoman(self, num: int) -> str:
        output = ''
        i = 3
        while i != -1:
            d = (num - num%(10**i))
            if d == 0:
                pass
            else:
                (lo, hi) = self.get_interval(d)
                if d/(10**i) == 4 or d/(10**i) == 9:
                    output += self.elementary[hi-d] + self.elementary[hi]
                elif lo == 1 or lo == 10 or lo == 100 or lo == 1000:
                    m = d // lo 
                    output += self.elementary[lo] * m
                else:
                    output += self.elementary[lo] + self.intToRoman(d - lo)
            num -= d
            i -= 1
        return output
