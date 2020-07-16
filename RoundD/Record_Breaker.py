t=int(input())

def out(tc,ss):
    print("Case #{}: {}".format(tc,ss))

def solve(T):
    days=int(input())
    streak=list(map(int,input().split()))
    sol=0
    M=-1
    for i in range(days):
        if streak[i]>M: 
            if i<days-1:
                if streak[i]>streak[i+1]: 
                    sol+=1
            else: 
                sol+=1
        if streak[i]>M:
            M=streak[i]
    out(T,sol)
    
for tc in range(1,t+1):
    solve(tc)