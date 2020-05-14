def findJudge(N, trust):
    peoples=[]
    if N == 1:
            return 1
    for pair in trust:
        if pair[0] not in peoples:
            peoples.append(pair[0])
        if pair[1] not in peoples:
                peoples.append(pair[1])       
    lc=dict()
    rc=dict()
    for pair in trust:
        left=pair[0]
        right=pair[1]
        if left not in lc:
            lc[left]=1
        else:
            lc[left]=lc[left]+1
        if right not in rc:
            rc[right]=1
        else:
            rc[right]=rc[right]+1
    print(lc,rc)
    for p in peoples:
        print("people = ",p)
        if p not in lc and rc[p] == N-1:
            return p
    return -1
d=[[1,2],[1,3],[2,1],[2,3],[1,4],[4,3],[4,1]]
print("judge",findJudge(4,d))