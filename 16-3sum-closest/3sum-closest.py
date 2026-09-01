class Solution(object):
    def threeSumClosest(self, nums, target):
       nums.sort()
       closest=nums[0]+nums[1]+nums[2]

       for i in range(len(nums)-2):
            fix=nums[i]
            left=i+1
            right=len(nums)-1

            while left < right:
                total=fix + nums[left] + nums[right]
            
                if abs(total-target) < abs(closest-target):
                    closest=total
                if total<target:
                  left+=1
                elif total>target:
                  right-=1
                else:
                  return total
       return closest
