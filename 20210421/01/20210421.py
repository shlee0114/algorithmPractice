import heapq 

def solution(numbers):
    maxVal = max(numbers)
    if maxVal == 0:
        return "0";
    maxIdx = len(str(maxVal))
    calcNum = []
    heapAns = []
    for i in numbers:
        tmpVal = 0
        for j in range(maxIdx):
            if j < len(str(i)) :
                tmpVal += int(str(i)[j]) * (10 ** (maxIdx - j))
            else :

                value = 0
                if len(str(i))  > j :
                    value = len(str(i)) % j
                elif len(str(i)) < j :
                    value = j % len(str(i))
                tmpVal += (int(str(i)[value])) * (10 ** (maxIdx - j) )
        calcNum.append(tmpVal)
    for idx, val in enumerate(calcNum):
        heapq.heappush(heapAns, [-val, idx])
    answer = ""
    for i in numbers:
        answer += str(numbers[heapq.heappop(heapAns)[1]])    
    return answer
9, 90, 908, 89, 898, 8, 1, 101, 10
987654321101000
print(solution([9, 90, 908, 89, 898, 8, 1, 101, 10]), 987654321101000)