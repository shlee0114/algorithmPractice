# 프로그래머스 위장

> 나의 코드
```Python
divisionCnt = {}
def solution(colthes) :
    for i in colthes:
        if divisionCnt.get(i[1]) == None :
            divisionCnt[i[1]] = 1
        else :
            divisionCnt[i[1]] += 1
    answer = 0
    tmp = 1
    for v in divisionCnt :
        tmp *= divisionCnt[v] + 1
    answer += tmp - 1
    return answer
```

## 코드 설명
```Python
    for i in colthes:
        if divisionCnt.get(i[1]) == None :
            divisionCnt[i[1]] = 1
        else :
            divisionCnt[i[1]] += 1
```
> 받은 데이터를 종류별로 갯수만 저장

```Python
    for v in divisionCnt :
        tmp *= divisionCnt[v] + 1
    answer += tmp - 1
```
> 경우의 수를 구함 +1을 해주는 이유는 선택을 하지않는 옵션도 있기에 +1을 해주고 전부 다 선택이 안되는 경우는 없기에 마지막에 +1을 해줌

## 프로그래머스 가장 좋아요를 많이 받은 코드

```Python
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
```
### 코드 설명(내가 작성한 코드가 아니라 부정확할 수 있음)

```Python 
    cnt = Counter([kind for name, kind in clothes])
```
> collections모듈의 Counter를 사용해서 clothes의 name(key)값의 수를 샌 값을 리턴한다,

```Python
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
```
> functools모듈의 reduce를 사용해서 cnt의 values를 사용해서 순환하면서 값을 구하는 방식 *이기에 초기값을 1로 설정했다.
cnt.values의 첫번째 값과 두번째 값이 앞에 람다식으로 넘어간 후 사용자가 정의한 내용대로 연산 후 연산된 값이 리턴된다
y에 1을 더한 이유는 입지않음이란 값또한 추가되어야하기에 1을 더했으며, 모두 안입는 경우는 없기에 마지막에 1을 뺴었다.