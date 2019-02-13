print("Enter the text")
T = input()
print("Enter the pattern")
P = input()
n = len(T)
m = len(P)

d = {} #Empty list

for j in range(0, m): #Mapping characters(keys) in the search string to their indexes(values)
    d[P[j]] = j

z = 0
i = 0
c = 0
match = [] #List to store the matching indexes

while i < n:
    c = 0
    for j in range(m - 1, -1, -1):
        lensub = 1
        if (i - (m - j - 1)) >= 0: #Guard for the list bound
            if T[i - (m - j - 1)] != P[j]:
                c = c + 1 #Counter for a mismatch
                index = d.get(T[i - (m - j - 1)], -1) #Finding the index of mismatched character in T, returns -1 if character is not present
                if index == -1: #If character isn't present in the prefix
                    lensub = len(P[0:j - 1])
                elif index < j: #Limiting checking for occurances of the mismatched character to only to the prefix of P
                    lensub = len(P[index:j - 1])
                break
    if (j == 0) & (c == 0):
        match.append(i - (m - 1)) #Appending the index if its a match
        z = z + 1 #Counting number of matches
    if lensub > 1:
        i = i + lensub
    else:
        i = i + 1

print("Number of matches found : {}".format(z))
if z != 0:
    print("Indexes in main string where matches were found :{}\n".format(match))
