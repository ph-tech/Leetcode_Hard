from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = sorted(Counter(arr).values(),reverse = True)
        half,removed,count = len(arr) / 2, 0, 0
        for f in freq:
            removed += f
            count += 1
            if removed >= half:
                return count
        