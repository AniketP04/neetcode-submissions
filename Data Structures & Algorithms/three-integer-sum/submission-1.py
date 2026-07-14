class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        nums.sort()

        for i, num in enumerate(nums):

            if num > 0:
                break
            
            if i > 0 and num == nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1
            while left < right:
                
                three_sum = num + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    answer.append([num, nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        return answer