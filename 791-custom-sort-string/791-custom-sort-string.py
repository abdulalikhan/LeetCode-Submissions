class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        freq2 = {}
        for item in order:
            if item not in freq:
                freq[item] = 1
        for item in s:
            if item in freq:
                if item not in freq2:
                    freq2[item] = 1
                else:
                    freq2[item] += 1
            else:
                freq[item] = 1
                if item not in freq2:
                    freq2[item] = 1
                else:
                    freq2[item] += 1
        ordered = ""
        for item in freq:
            if item in freq2:
                ordered += item*freq2[item]
        return ordered