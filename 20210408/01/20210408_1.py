from collections import deque
def solution(prices):
    _price = deque(prices)
    answer = []
    while _price :
        cnt = 0
        data = _price.popleft()
        for i in _price:
            cnt+=1
            if data > i :
                break
        answer.append(cnt)
    return answer