class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a freq array representing frequency[cnt]
        freq_arr = [[] for i in range(len(nums) + 1)]

        count = collections.defaultdict(int)
        for num in nums:
            count[num] += 1
        
        for num, cnt in count.items():
            freq_arr[cnt].append(num)
        
        res = []
        for i in range(len(freq_arr) - 1, 0, -1):
            res.extend(freq_arr[i])
            if len(res) >= k:
                break
        
        return res[:k]

        