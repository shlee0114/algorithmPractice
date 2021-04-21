from collections import deque

def solution(citations):
    citations.sort()
    cenVal = len(citations) // 2
    if citations[cenVal] < len(citations[cenVal::]) :
        citations = citations[cenVal::]
        cenVal = citations[0]
        while True :
            cenVal+=1
            if cenVal in citations :
                citations.pop()

            if cenVal >= len(citations) :
                return cenVal
    else :



print(solution([3, 0, 6, 1, 5]))