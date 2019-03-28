from array import *

tests = int(input())
jumps = []
for t in range(tests):
    s = int(input())
    if s != 0:
        i = input()
        r = i.split()
        # print(r)
        r.insert(0, s)
        jumps.append(r)
    else:
        r = [0]
        jumps.append(r)


for i in range(tests):
    highJump = 0
    lowJump = 0
    tam = jumps[i][0]
    if tam != 0:
        ans = jumps[i][1]
        for j in range(1, tam+1):
            if(jumps[i][j] > ans):
                highJump = highJump + 1
            elif(jumps[i][j] < ans):
                lowJump = lowJump + 1
            
            ans = jumps[i][j]

    print("Case {}: {} {}".format(i+1, highJump, lowJump))
