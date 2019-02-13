print("Enter the text")
T = input()
print("Enter the pattern")
P = input()
n = len(T)
m = len(P)

z = 0
i = 0
c = 0
match = [] #List to store the matching indexes

while i < n:
    c = 0
    for j in range(0, m):
        if (i + j) < n: #Guard for the list bound
            if T[i + j] != P[j]:
                c = c + 1 #Counter for a mismatch
                break
    if (j == m - 1) & (c == 0):
        match.append(i) #Appending the index if its a match
        z = z + 1 #Counting number of matches
    i = i + 1

print("Number of matches found : {}".format(z))
if z != 0:
    print("Indexes in main string where matches were found :{}\n".format(match))
