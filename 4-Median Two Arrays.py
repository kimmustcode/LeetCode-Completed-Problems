# Runtime: 7 ms (14.55%) 
# Memory: 19.5 mb (77.64%)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        fulllength = len(nums1) + len(nums2)
        mid = (fulllength // 2) - 1
        check = fulllength % 2 
        temp = [] 
        i = 0 
        j = 0 

        while True:
            if i > len(nums1) - 1: 
                temp.extend(nums2[j:]) 
                return ((temp[mid] + temp[mid+1]) / 2) if check == 0 else float(temp[mid + 1])
            elif j > len(nums2) - 1:
                temp.extend(nums1[i:])
                return ((temp[mid] + temp[mid+1]) / 2) if check == 0 else float(temp[mid + 1])

    
            if nums1[i] < nums2[j]:
                temp.append(nums1[i])
                i += 1
            else: 
                temp.append(nums2[j])
                j += 1 
        