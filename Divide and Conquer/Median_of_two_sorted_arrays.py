# https://leetcode.com/problems/median-of-two-sorted-arrays/
def findMedianSortedArrays(nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        m=len(nums1)//2
        if len(nums1)%2!=0:
            return nums1[m]
        else:
            return (nums1[m-1]+nums1[m])/2

nums1 = [1,3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))
