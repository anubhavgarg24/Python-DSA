
def longestNonDup(s):
    map = {}
    l=0
    r=0
    n=len(s)
    longest = 0
    while(l<n and r<n):
        ele = s[r]
        if(ele in map): # move the left pointer to max(l, previous encounter+1) => map[ele] + 1
            l = map[ele]+1
        # if not in map already add, else update the new index
        map[ele] = r # assign the value to key
        longest = max(longest, r-l+1)
        r+=1
    return longest

string = "abaacad"
print(longestNonDup(string)) # cad