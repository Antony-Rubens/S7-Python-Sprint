nums=[1,2,3,4,5]

left=0
right=len(nums)-1

while left<right:
    print(nums[left],nums[right])

    left+=1
    right-=1