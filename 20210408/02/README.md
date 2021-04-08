# 프로그래머스 기능개발

> **내 코드**
```Python
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
```
### ***코드 분석***
+ 기본 설명
> 가장 앞에 있는 progresses번호에 해당하는 speeds의 값들을 더하다가 가장 앞에 있는 progresses값이 100이 넘으면 그 뒤에 있는 값들 중 100이 넘는 값들을 조회한다 조회 후 한 번에 100이 넘는 얘들을 몇개를 보냈는지를 리턴하는 문제이다.

+ 구성
> 구성은 간단하다 배열로 넘어온 값들을 dequeue로 변환한 후 반복하면서 데이터를 더해주고, 가장 앞의 값이 100이 넘었는 지 체크한다.
* 코드
```Python
        if progresses[0] >= 100 :
            speeds.popleft()
            progresses.popleft()
            total += 1
```
> 만약 가장 앞의 progresses값이 100이 넘었을 시 speeds와 progresses모두 가장 앞의 값을 지워준 후 total값에 1을 더해준다.
```Python
        else :
            if total != 0 :
                answer.append(total)
                total = 0
            for i in range(len(speeds)):
                progresses[i] += speeds[i]
```
>만약 100이 넘지 않았을 시 total값이 0이 아닐 시 리턴해주는 배열에 total값을 넣고 total값을 초기화한다.
그 후 남은 progresses에 speeds를 더해준다.
>>total이 총 몇개의 progresses가 한 번에 사라졌는 지 확인하는 변수다.

### 프로그래머스 가장 추천수가 높은 코드
```Python
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
```

+ 코드 분석
``` Python
    for p, s in zip(progresses, speeds):
```
> progresses와 speeds를 zip으로 묶어서 한 번에 배열을 돌린다.
```Python
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
```
>위 코드는 세분하게 나누어서 봐야한다.
우선 **((p-100)//s)** 이 부분은 해당 progresses에 100을 뺸 후 남은 값을 speeds로 나눠서 몇 번의 speeds를 더해야지 100이 넣는 횟수를 구한다. 만약 Q에 들어가 있는 마지막 값하고 비교했을 떄 넣는 횟수가 더 많을 경우 Q에 비교하는 값을 교체한다.

```Python
        else:
            Q[-1][1]+=1
```
>만약 더해줘야하는 횟수가 적을 시 가장 앞에 있는 값이 끝나면 자동으로 끝나기 떄문에 같이 끝나는 횟수를 더해준다.

## 후기
상당히 신기했다. 나는 단순하게 더해서 100을 만들생각만 했지 위와 같이 더해야 하는 횟수를 구해서 해당 횟수로 계산하는 방법은 생각치도 못했다 이로 인해 나는 한 번만 반복하면 될 문제를 몇배를 더 반복한 것이 된다. 항상 이런 다양한 가능성을 열어서 생각해야 겠다.
