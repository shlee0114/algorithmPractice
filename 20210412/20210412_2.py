import heapq

def solution(scoville, k):
    heapq.heapify(scoville)
    
    cnt = 0
    while scoville[0] < k :
        if len(scoville) == 1:
            return -1
        value = 0
        firstVal = heapq.heappop(scoville)
        secondVal = heapq.heappop(scoville)
        value = firstVal + (secondVal * 2)
        heapq.heappush(scoville, value)
        cnt+=1
    
    return cnt



print(solution( [ 1,1,2 ] , 3), 1)
print(solution([1, 2], 3), 1)
print(solution([1, 1, 1], 4), 2)
print(solution([10, 10, 10, 10, 10], 100), 4)
print(solution([1, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 0, 3, 9, 10, 12], 7), 3)
print(solution([0, 0, 0, 0], 7), -1)
print(solution([0, 0, 3, 9, 10, 12], 7000), -1)
print(solution([0, 0, 3, 9, 10, 12], 0), 0)
print(solution([0, 0, 3, 9, 10, 12], 1), 2)
print(solution([0, 0], 0), 0)
print(solution([0, 0], 1), -1)
print(solution([1, 0], 1), 1)