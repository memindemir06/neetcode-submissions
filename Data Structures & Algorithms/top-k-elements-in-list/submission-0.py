class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        return [i[0] for i in (sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k])]