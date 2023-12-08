#permutation
size = int(input("Input the size of set: "))
the_set = [0]*size
for i in range(size):
    the_set[i] = int(input("Input the number of the set: "))

permutation = []
def generatePermutation():
        #uses dfs and visited dp
        visited = [False] * len(the_set)
        def dfs(temp):
            if len(temp) == len(the_set) and temp not in permutation:
                permutation.append(temp[:])
                return
            for i in range(len(the_set)):
                if not visited[i]:
                    if not(i>0 and not visited[i-1] and the_set[i]==the_set[i-1]):
                        visited[i] = True
                        dfs(temp+[the_set[i]])
                        visited[i] = False
        dfs([])
        return permutation
        
generatePermutation()
permutation = sorted(permutation)
print(f"Your permutation is: {permutation}")
