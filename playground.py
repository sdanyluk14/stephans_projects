from collections import deque, defaultdict
nums = [2,3,1,1,4]
nums2 = [3,2,1,0,4]

def canJump(nums) -> bool:
        dic = defaultdict(bool)

        # Is dynamic programming necessary?
        def dp(i):
            if i >= len(nums)-1:
                return True
            
            if i in dic:
                 return dic[i]
            
            dic[i] = False
            
            # Remember - can jump up to this many spaces
            for j in range(nums[i]+1):
                if dp(i+j):
                    dic[i] = True

            return dic[i]    
            
        dp(0)
        return dic[0]

print(canJump(nums2))