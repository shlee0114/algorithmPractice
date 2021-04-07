# 프로그래머스 다리를 지나는 트럭

**나의 코드**
```Python
def solution(bridge_length, weight, truck_weights):
    goingTruck = []
    truckTime = []
    totalweight = 0
    answer = 1
    while truck_weights or goingTruck :
        if truck_weights :
            totalweight += truck_weights[0]
            if totalweight <= weight :
                goingTruck.append(truck_weights.pop(0))
                truckTime.append(answer)
            else :
                totalweight -= truck_weights[0]
        
        answer += 1
        if (answer  - truckTime[0]) % bridge_length == 0 :
           totalweight -= goingTruck.pop(0)
           truckTime.pop(0)
    return answer
```

>**코드해석**
```Python
    while truck_weights or goingTruck :
```
> 사용자가 입력한 트럭의 수와 다리를 지나가는 트럭을 저장한 배열들이 없어지면 반복문이 종료된다.

```Python
        if truck_weights :
            totalweight += truck_weights[0]
            if totalweight <= weight :
                goingTruck.append(truck_weights.pop(0))
                truckTime.append(answer)
            else :
                totalweight -= truck_weights[0]
```

>잔여 트럭데이터가 있을 시 전체 트럭의 무게에 현재 들어가야할 트럭의 무게를 더한 후 해당 무게가 다리의 무게를 넘어가는 지 체크 후 넘어가면 원복하고 안넘어갈 시 goingTruck에 데이터를 추가하고 truckTime에 현재 트럭이 들어간 시간을 저장한다.

```Python
        answer += 1
        if (answer  - truckTime[0]) % bridge_length == 0 :
           totalweight -= goingTruck.pop(0)
           truckTime.pop(0)
```

>현재 진행시간에서 트럭이 지나간 시간을 뺀 후 다리 진행시간을 나눈 나머지 값이 0이면 전체 무게에서 해당 트럭을 뺴준 후 트럭 타임에도 제거해서 다음 트럭타임이 오도록 한다.
이렇게 해서 최종 answer값을 리턴해준다
>> answer에 1을 더해주는 작업을 선행한 이유는 선행하지 않으면 넣자마자 바로 if문 내부로 넘어가기 때문

### 후기
처음에는 조건문에 len() > 0으로 배열에 값이 존재하는 지 체크했지만 python에서는 그냥 배열만 입력하면 해당 배열에 값이 존재하는 지 체크하기에 len으로 배열의 값을 체크할 필요도 없고 실제로 속도도 훨씬 느리기에 len은 지양하는 것이 좋은 거 같다.

## **프로그래머스 추천수가 가장 많은 코드**
```Python
import collections

DUMMY_TRUCK = 0

class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count
```

### 주관적인 코드 분석

>bridge class
```Python
    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0
```
> bridge클래스를 생성 시 작동하는 초기화 모듈 bridge클래스에 maxLengrh, maxWeight를 사용자에게 받아서 저장하고 queue, currentWeight는 새로 생성한다.

```Python
    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False
```
>사용자가 입력한 값(최대 무게, 최대 길이)를 넘지 않는 이상 queue라는 배열에 데이터를 입력히고 현재 무게를 압데이트한다 입력될 시 True 아닐 시 False로 반환한다.

```Python
    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item
```

>큐의 처음에 입력한 값을 제거 하고 현재무게에서 그만큼 뺸다.

```Python
    def __len__(self):
        return len(self._queue)
```
> 큐의 길이 반환

```Python
    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))
```

>데이터 출력용

>solution

```Python
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)
```
> bidge class에 사용자가 입력한 데이터를 넣으면서 선언 truck에는 트럭 무게로 내부를 저장한다 또한 trucks와 bridge간 길이가 같아야 하므로 내부를 더미데이터로 채운다.

```Python
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1
```

>bridge를 한 칸 비워둔 다음 bridge class의 push로 데이터를 보낸 다음 내부 조건이 충족되어 데이터가 입력되었다면 입력한 데이터는 지우고 입력되지 않았다면 원래대로 더미데이터를 넣는다.

```Python
    while bridge:
        bridge.pop()
        count += 1
```

> 트럭의 데이터가 전부 지워졌다면 나머지 bridge에 있는 데이터를 지우는 작업

후기

큐로 pop만 있는 것으로 알았지만 파이썬에는 dequeue로 하나가 더 존재하며 pop(0)은 지운다음 하나씩 자리를 당기는 작업때문에 O(n)의 시간이 걸리지만 popleft는 앞에 하나만 지우고 시작 주소값만 변경해주는 거 같아서 O(1)이 걸린다 추후에 또 큐를 사용할 일이 있으면 pop(0)보다는 popleft를 사용하는 방향으로 코드를 작성해야겠다.