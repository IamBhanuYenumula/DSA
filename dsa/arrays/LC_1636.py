class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        freq = {}
        result = []
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        sorted_freq = sorted(freq.items(), key = lambda x:(x[1],-x[0]))
        for i in sorted_freq:
          for j in range(i[1]):
            result.append(i[0])
        return result

  
nums = [2,3,1,3,2]
print(Solution().frequencySort(nums))