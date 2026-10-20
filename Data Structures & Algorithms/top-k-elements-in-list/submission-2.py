# from collections import Count
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        # print(c)
        top_k = c.most_common(k)
        ans = []
        for i in top_k:
            ans.append(i[0])
        return ans