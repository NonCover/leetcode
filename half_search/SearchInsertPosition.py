# @author: noc @time: 2019年12月18日
def Solution(nums, target):
    '''
    :param nums: 无重复有序数组
    :param target: 插入的值
    :return: 插入的位置
    '''
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = nums[mid]
        if guess < target:
            low = mid + 1
        else:
            high = mid - 1
    return low

res = Solution([1,3,5,6], 0)
print(res)