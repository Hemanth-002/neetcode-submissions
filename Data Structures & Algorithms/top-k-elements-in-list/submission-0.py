from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        sorted_by_values = dict(sorted(freq.items(),key=lambda item:item[1],reverse=True))

        return list(sorted_by_values.keys())[:k]