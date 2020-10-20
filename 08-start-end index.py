# Find the start and end index of a target element

def start(arr, target):
    left=0
    right=len(arr)-1
    
    while(left<=right):
        mid=left + (right-left)//2
        if(arr[mid]==target):
            # check if prev. ele is target or mid == 0
            if(mid-1>=0 and arr[mid-1]!=target or mid==0):
                return mid
            else: # move backward
                right = mid-1
        elif(arr[mid]<target):
            left = mid+1
        elif(arr[mid]>target):
            right = mid-1
    return -1

def end(arr, target):
    left=0
    right=len(arr)-1
    
    while(left<=right):
        mid=left + (right-left)//2
        if(arr[mid]==target):
            # check if next ele is target or mid == len(arr)-1
            if(mid+1<len(arr) and arr[mid+1]!=target or mid==len(arr)-1):
                return mid
            else: # move forward
                left = mid+1
        elif(arr[mid]<target):
            left = mid+1
        elif(arr[mid]>target):
            right = mid-1
    return -1

arr = [10, 11, 11, 11, 13, 13, 14, 15]
target = 11
print("start:",start(arr, target), end=", ")
print("end:",end(arr, target))