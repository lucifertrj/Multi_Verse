def searchRange(nums,target):
    if target not in nums:
        return [-1,-1]
    ans = []
    beg,end=0,len(nums)
    while beg<=end:
        mid = (beg+end)//2
        if nums[mid] == target:
            ans.append(mid)
            ans.sort()
        elif nums[mid]<target:
            beg=mid+1
        else:
            end=mid-1
    return -1
print(searchRange([5,7,8,8,10],10))

