import heapq as hq

def solution(operations) :
    valArray = []
    maxHeap = []
    minHeap = []
    for i in operations:
        if i[0] == "I":
            valArray.append(int(i[2:]))
            hq.heappush(maxHeap, [-int(i[2:]), int(i[2:])])
            hq.heappush(minHeap, int(i[2:]))
        elif i == "D 1":
            if len(minHeap) == 0:
                continue
            hq.heappop(maxHeap)
            minHeap = []
            for j in maxHeap :
                hq.heappush(minHeap, j[1])
        elif i == "D -1":
            if len(minHeap) == 0:
                continue
            hq.heappop(minHeap)
            maxHeap = []
            for j in minHeap :
                hq.heappush(maxHeap, [-j, j])
    
    if len(minHeap) == 0:
        return [0,0]
    return [hq.heappop(maxHeap)[1], hq.heappop(minHeap)]


print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))