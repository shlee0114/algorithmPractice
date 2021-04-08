# 프로그래머스 주식가격
## **내 코드**
```Python
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
```

+ 코드 해석
```Python
    while _price :
        cnt = 0
        data = _price.popleft()
        for i in _price:
            cnt+=1
            if data > i :
                break
        answer.append(cnt)
```
> popleft를 사용하기 위해 변환한 dequeue인 _price의 배열이 없어질 떄까지 반복한다. **data = _price.popleft**에서 하단에 있는 데이터를 뽑는다.
```Python
        for i in _price:
            cnt+=1
            if data > i :
                break
```
>추출한 데이터와 그 외의 데이터를 비교하면서 추출한 데이터보다 작은 데이터가 나올 시 멈추면서 cnt값을 반환 큐에 넣어준다.

+ **스택을 사용한 코드**
```Python
def solution(p):
    ans = [0] * len(p)
    stack = [0]
    for i in range(1, len(p)):
        if p[i] < p[stack[-1]]:
            for j in stack[::-1]:
                if p[i] < p[j]:
                    ans[j] = i-j
                    stack.remove(j)
                else:
                    break
        stack.append(i)
    for i in range(0, len(stack)-1):
        ans[stack[i]] = len(p) - stack[i] - 1
    return ans
```

+ ***코드해석***
```Python
    ans = [0] * len(p)
```
>받은 배열의 크기만큼 0이 들어가있는 배열 생성
```Python
    for i in range(1, len(p)):
```
>처음 숫자는 무조건 0이므로 1부터 시작한다
```Python
        if p[i] < p[stack[-1]]:
```
>현재 보고있는 값과 스택에 마지막으로 들어간 값(가장 최근 값)과 비교해서 최근 값이 크면 아래에 있는 식을 돌린다.
```Python
            for j in stack[::-1]:
                if p[i] < p[j]:
                    ans[j] = i-j
                    stack.remove(j)
                else:
                    break
```
>스택 내부에 들어간 값을 마지막부터 0까지 역순으로 조회한다.
만약 조회 중 현재 값과 스택 내부에 있는 값과 비교 후 스택 내부 값이 더 크면 해당 스택의 번호에 해당하는 ans내부에 현재 번호와 해당 스택의 번호를 계산해서 저장후 해당 스택은 삭제한다.
```Python
        stack.append(i)
```
>그 다음 스택에 현재 번호를 저장한다.
```Python
    for i in range(0, len(stack)-1):
        ans[stack[i]] = len(p) - stack[i] - 1
```
>만약 끝까지 작은 값이 없어서 스택 내부에 저장되어있는 값들을 전체 값과 비교해서 ans내부에 저장 후 값을 리턴한다.

+ 후기

개인적으로 추천수가 가장 높진 않지만 스택을 사용했으며, 큐를 사용한 알고리즘들은 O(n^2)의 속도를 가지지만 스택은 O(n)의 속도를 가진다는 것이 신기하고 분석해보고 싶어서 가져왔다