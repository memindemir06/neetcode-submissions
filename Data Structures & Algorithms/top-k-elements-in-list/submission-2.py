class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        # return [i[0] for i in (sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k])]

        bucket = [[] for i in range(len(nums) + 1)]

        for num, fr in freq.items():
            bucket[fr].append(num)
    
        result = []

        for group in bucket[::-1]:
            for num in group:
                if len(result) < k:
                    result.append(num)
                else:
                    return result

        return result
            
            
