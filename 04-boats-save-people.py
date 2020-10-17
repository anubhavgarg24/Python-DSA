# two pointer approach
def savePeople(arr, k):
    arr.sort()
    left = 0
    right = len(arr) - 1
    boats = 0
    while(left<=right):
        if(left==right):
            boats +=1 # carry the person alone
            break

        # Now start comparing the weights
        elif(arr[left] + arr[right]<=k): # carry the heaviest & lightest person together
            left +=1
            
        right -=1
        boats +=1 
        # carry the heaviest person alone
        # else: 
        #     right -=1
        #     boats +=1 
    return boats

arr = [1, 2, 3, 3]
limit = 3
ans = savePeople(arr, limit)
# worst case we will take maximum boats = no. of people
# as max+_weight <=limit
print("min boats: %d"%ans)