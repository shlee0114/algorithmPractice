from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    total = 0
    while progresses:
        if progresses[0] >= 100 :
            speeds.popleft()
            progresses.popleft()
            total += 1
        else :
            if total != 0 :
                answer.append(total)
                total = 0
            for i in range(len(speeds)):
                progresses[i] += speeds[i]
    answer.append(total)
    return answer