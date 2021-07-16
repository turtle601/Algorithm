### leetcode 1
## Two Sum
# 덧셈하여 타겟을 만들 수 있는 배열의  두 숫자 인덱스를 리턴하라. 

# 입력값 : 
nums = [2,7,11,15], target = 9

class Solution:
    def twoSum(self, nums, target):
        dic = {}
        
        # 값에 대한 주소값을 dic 자료형에 저장
        for i, num in enumerate(nums):
            if target - num in dic.keys():
                return [dic[target-num],i]
            
            dic[num] = i