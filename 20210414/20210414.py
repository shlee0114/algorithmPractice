import heapq as hq


def solution(jobs):
    i, answer, now = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs) :
        for j in jobs :
            if start < j[0] <= now :
                hq.heappush(heap, [j[1], j[0]])
        if len(heap) != 0 :
            current = hq.heappop(heap)
            start = now
            now += current[0]
            answer += now - current[1]
            i+=1
        else :
            now += 1
    return answer // len(jobs)
print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
print(solution([[0, 3], [1, 9], [2, 6]]), 9)
print(solution([[0, 1]]), 1)
print(solution([[1000, 1000]]), 1000)
print(solution([[0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
print(solution([[0, 1], [1000, 1000]]), 500)
print(solution([[100, 100], [1000, 1000]]), 500)
print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]), 7)