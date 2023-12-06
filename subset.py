#subsets
size = int(input("Input the size of set: "))
the_set = [0]*size
for i in range(size):
    the_set[i] = int(input("Input the number of the set: "))

ans = []
def generateSubset(start, temp):
    ans.append(temp[:])
    for i in range(start, size):
        temp.append(the_set[i])
        generateSubset(i+1, temp)
        temp.pop()
        
generateSubset(0, [])
print(f"Your subset is: {ans}")
