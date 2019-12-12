#  leetcode.4. 寻找两个有序数组的中位数
# @level: 困难 @author:noc  @time:2019年12月12日
class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2    
        nums.sort()
        if len(nums) % 2 == 1:
            middle = nums[len(nums) // 2 ]
        else:
            middle = nums[(len(nums) // 2 )] + nums[(len(nums) // 2 - 1)]
            res = middle / 2
            return res
        return middle # -1 1 2 3 
  
