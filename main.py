
def merge(x1, x, y1, y):
    #x1 is length x + y. The first x elements are the 'real' x1 and the rest are the space for the y1 elements
    #y is unused - we simply iterate over y1
    offset = 0
    for item in y1:
        x1[x+offset] = y1[offset]
        offset += 1
    x1.sort() #Python sort() time complexity is O(NlogN).
    return x1

#Example 1:
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1, m, nums2, n))

#Example 2:
nums1 = [1]
m = 1
nums2 = []
n = 0
print(merge(nums1, m, nums2, n))

#Example 3:
nums1 = [0]
m = 0
nums2 = [1]
n = 1
print(merge(nums1, m, nums2, n))
