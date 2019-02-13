print("Enter the text")
T = input()
print("Enter the pattern")
P = input()
n = len(T)
m = len(P)

cache = [0] * m # Precomputing cache to store the length of the repeating string
for j in range(0, m):
    lensub = 1
    for k in range(0, j):
        if P[0:k] == P[j - k:j]:
            if len(P[0:k]) > lensub:
                lensub = len(P[0:k])
    cache[j] = lensub

z = 0
i = 0
c = 0
match = [] #List to store the matching indexes

while i < n:
    c = 0
    for j in range(0, m):
        lensub = 1
        if (i + j) < n: #Guard for the list bound
            if T[i + j] != P[j]:
                c = c + 1 #Counter for a mismatch
                lensub = cache[j] #Accessing cache to find the shift distance in case of a mismatch
                break
    if (j == m - 1) & (c == 0):
        match.append(i) #Appending the index if its a match
        z = z + 1 #Counting number of matches
    i = i + lensub #Shifting by the length of repeating string

print("Number of matches found : {}".format(z))
if z != 0:
    print("Indexes in main string where matches were found :{}\n".format(match))
