# IN THE ARRAY, point(i, a[i]): i->x-coordinate & a[i]->y-coordinate
# n vertical lines are drawn using these points on x-axis
# Find the max water that can be stored b/w two lines

# Sol: Find the max area b/w the lines

#  two-pointer approach
def maxWater(arr):
    left = 1
    right = len(arr)-1
    maxArea = 0
    while(left<right):
        # smaller side * dis on x-axis
        currentArea = min(arr[left], arr[right]) * (right-left)

        maxArea = max(maxArea, currentArea)
        if(arr[left]<arr[right]): #stay w/ the bigger side
            left+=1
        else:
            right-=1
    return maxArea

arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxWater(arr))