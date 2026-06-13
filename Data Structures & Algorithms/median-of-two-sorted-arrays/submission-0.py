class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalList = nums1 + nums2
        totalList.sort()
        returnValue = 0

        if len(totalList) % 2 is 0:
            value1 = totalList[int(len(totalList)/2) - 1]
            print(int(len(totalList)/2))
            print(value1)
            value2 = totalList[int(len(totalList)/2)]
            print(value2)
            return (value1 + value2)/2

        else:
            return totalList[int(len(totalList)/2)]
        
        return totalList