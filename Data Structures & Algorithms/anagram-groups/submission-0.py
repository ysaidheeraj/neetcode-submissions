from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        seen = set()
        counters = [Counter(strs[i]) for i in range(len(strs))]
        for i in range(len(strs)):
            if i not in seen:
                seen.add(i)
                partial_result = [strs[i]]
                for j in range(i+1, len(strs)):
                    if j not in seen and counters[j] == counters[i]:
                        partial_result.append(strs[j])
                        seen.add(j)
                result.append(partial_result)
        return result
            