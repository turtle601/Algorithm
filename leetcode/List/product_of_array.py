# 238. Product of Array Except Self

# 문제 : 배열을 입력받아 output[i]가 자신을 제외한 
# 나머지 모든 요소의 곱셈 결과가 되도록 출력하라

# 시간 복잡도 O(n)
# 나눗셈 X

# input : [1,2,3,4]
# output : [24,12,8,6]

def productExceptSelf(nums):
  
  result = []
  
  # 왼쪽 곱셈 
  left = 1

  for num in nums:
    result.append(left)
    left *= num 
  
  # 오른쪽 곱셈
  right = 1

  for idx in range(len(nums)-1,-1,-1):
    result[idx] *= right
    right *= nums[idx] 

  return result

productExceptSelf([1,2,3,4])

