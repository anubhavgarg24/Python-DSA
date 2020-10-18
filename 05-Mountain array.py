# Find whether array is first inc. then dec. -> like mountain
# true or false

def checkMount(arr):
    i=1
    n = len(arr)

    # check if n > 3 -> else it can't be inc. then dec.
    if(n<3):
        return False
    # move i till inc.
    while(i < n and arr[i] > arr[i-1]):
        i+=1

    # check if i is still 1 or moved till end
    if(i==1 or i==n):
        return False
    while(i < n and arr[i] < arr[i-1]):
        i+=1

    # return true or false-> if i reached end or not
    return i==n

arr = [0, 2, 3, 4, 5, 2, 1]
# ->false
# arr = [1, 3] 
# -> true
# arr = [1, 5, 2] 
print(checkMount(arr))