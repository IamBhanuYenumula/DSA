from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
      profile = list(zip(names,heights))
      sorted_profile = sorted(profile,key=lambda x:x[1], reverse = True)
      return [x[0] for x in sorted_profile]




names = ["Mary","John","Emma"]
# names = ["Alice","Bob","Bob"]
heights = [180,165,170]
# heights = [155,185,150]

print(Solution().sortPeople(names,heights))