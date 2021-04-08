def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q) != 0 :
            print(Q, Q[-1][0], ((p-100)/s), Q[-1][0]<-((p-100)//s))
        if len(Q)==0 or Q[-1][0]>((p-100)//s):
            Q.append([((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))