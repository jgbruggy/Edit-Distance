#Jeffrey Bruggeman

def edit_distance(s1, s2):
    
    m=len(s1)+1
    n=len(s2)+1
    
    mTable = {}
    for i in range(0, m):
        for j in range(0, n):
            mTable[i, j] = 0

for i in range(0, m):
    mTable[i,0]=i
    
    for j in range(0, n):
        mTable[0,j]=j
    
    for i in range(1, m):
        for j in range(1, n):
            if s1[i-1]==s2[j-1]:
                mTable[i, j] = min(mTable[i-1,j-1], mTable[i-1,j], mTable[i,j-1])
            else:
                mTable[i, j] = 1 + min(mTable[i-1,j-1], mTable[i-1,j], mTable[i,j-1])

print("Edit Distance Matrix\n")
print("       ", end='')
for j in range(n-1):
    print("| " + s2[j] + " ", end='')
    print("\n")
    for i in range(0, m):
        if i == 0:
            print("   ", end='')
        if i > 0:
            print(" " + s1[i - 1] + " ", end='')
        for j in range(0, n):
            print("| " + str(mTable[i, j]) + " ", end='')
        print("\n")

return mTable, mTable[m - 1, n - 1]

def get_edits(s1, s2, mTable, nEditDist):
    m = len(s1) + 1
    n = len(s2) + 1
    
    i_old = m - 1
    j_old = n - 1
    i_new = m - 1
    j_new = n - 1
    sOperation = ""
    nIndexOfOperation = nEditDist - 1
    sOperationList = {}
    for i in range(0, nEditDist - 1):
        sOperationList[i] = ""
    while 1:
        nLeft = mTable[i_old, j_old-1]
        nUp   = mTable[i_old-1, j_old]
        nUpLeft = mTable[i_old-1, j_old-1]
        if nUpLeft <= nLeft and nUpLeft <= nUp:
            i_new = i_old - 1
            j_new = j_old - 1
            if mTable[i_old, j_old] > nUpLeft:
                sOperation = "Move the character "+s2[i_old-1]+ " from "+ s2 + " to "+s1[j_old-1] +" in " +s1
                sOperationList[nIndexOfOperation] = sOperation
                nIndexOfOperation -= 1
        elif nLeft <= nUpLeft and nLeft <= nUp:
            i_new = i_old
            j_new = j_old - 1
            if mTable[i_old, j_old] > nLeft:
                sOperation = "Delete the character "+s2[i_old]+ " from " + s2
                sOperationList[nIndexOfOperation] = sOperation
                nIndexOfOperation -= 1
        elif nUp <= nUpLeft and nUp <= nLeft:
            i_new = i_old - 1
            j_new = j_old
            if mTable[i_old, j_old] > nUp:
                sOperation = "Add the character "+s1[j_old] + " to " + s1
                sOperationList[nIndexOfOperation] = sOperation
                nIndexOfOperation -= 1
        i_old = i_new
        j_old = j_new
        if i_old == 0 and j_old == 0:
            break

print("the sequence of the edits:")
for i in range(0, nEditDist):
    print("Step " + str(i + 1) + " : " + sOperationList[i])


if __name__ == "__main__":
    # Example 1
    #sString1 = "kitten"
    #sString2 = "sitting"
    # Example 2
    sString1 = "GAMBOL"
    sString2 = "GUMBO"
    mTable, nEditDist = edit_distance(sString1, sString2)
    print("Edit distance is " + str(nEditDist))
    get_edits(sString1, sString2, mTable, nEditDist)
