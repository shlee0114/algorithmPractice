from collections import deque

def solution(citations):
    citations.sort()
    citations = deque(citations)
    maxVal = max(citations)
    hIndex = 0
    print(citations)
    while citations :
        if citations[0] <= hIndex :
            citations.popleft()
        if hIndex >= len(citations) : 
            return hIndex    
        if hIndex != maxVal :
            hIndex+=1
    return hIndex
        

print(solution([1, 1,0, 0]))

