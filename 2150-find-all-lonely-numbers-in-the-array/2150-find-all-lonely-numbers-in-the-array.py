class Solution(object):
    def findLonely(self, nums):
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        lonelynums = []
        for x in d:
            if d[x] == 1 and (x+1) not in d and (x-1) not in d:
                lonelynums.append(x)
        return lonelynums