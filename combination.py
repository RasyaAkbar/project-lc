# combination from 1 to n with the mixed combination of k
k = int(input("Enter how many mixed combination: "))
n = int(input("Enter the number combination: "))
comb = []


def generateCombination(temp, k, n, start):
    if k == 0:
        comb.append(temp[:])
    for i in range(start, n + 1):
        temp.append(i)
        generateCombination(temp, k - 1, n, i + 1)
        temp.pop()


generateCombination([], k, n, 1)
print(comb)
