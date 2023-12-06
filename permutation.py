#permutation
size = int(input("Input the size of set: "))
the_set = [0]*size
for i in range(size):
    the_set[i] = int(input("Input the number of the set: "))

ans = []
def generatePermutation(start, temp):
    if len(temp) == len(the_set):
        ans.append(temp[:])
        return
    for i in range(size):
        if the_set[i] in temp:
            continue
        temp.append(the_set[i])
        generatePermutation(i+1, temp)
        temp.pop()
        
generatePermutation(0, [])
print(f"Your permutation is: {ans}")
