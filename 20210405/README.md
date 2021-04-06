# 프로그래머스 전화번호 목록
속도 170ms(프로그래머스 예제 가장 느린 기준)
전체 코드

```Python
firstKey = {}
def solution(phone_book):
    phone_book.sort(key = len)
    idx = len(phone_book[0])
    for i in range(len(phone_book)) :
        if firstKey.get(phone_book[i][0:idx]) == None:
            firstKey[phone_book[i][0:idx]] = []
            firstKey[phone_book[i][0:idx]].append(phone_book[i])
            continue
        else:
            for j in firstKey[phone_book[i][0:idx]] :
                if j == phone_book[i][0:len(j)]:
                    return False
            firstKey[phone_book[i][0:idx]].append(phone_book[i])
    return True
```
## 소스 설명
전달받은 배열을 정렬 후 해시 테이블의 기본 키의 길이선언
```Python
    phone_book.sort(key = len)
    idx = len(phone_book[0])
```
> 글자길이로 정렬을 하는 이유는 해시 테이블의 기본 키의 길이를 구하는 목적도 있으나, 길이 순으로 정렬해야지 추후에 값을 비교할 떄 한쪽 방향으로만 비교할 수 있어서 속도에 굉장한 영향을 끼침
>> sort내에 입력한 값은 글자의 길이로만 정렬하겠다는 의미
```Python
        if firstKey.get(phone_book[i][0:idx]) == None:
            firstKey[phone_book[i][0:idx]] = []
            firstKey[phone_book[i][0:idx]].append(phone_book[i])
            continue
```
> 배열을 돌리는 중 선언한 길이만큼 해당 배열을 자른 다음 자른 값을 키로 테이블이 없을 시 새로 생성한다.

```Python
        else:
            for j in firstKey[phone_book[i][0:idx]] :
                if j == phone_book[i][0:len(j)]:
                    return False
            firstKey[phone_book[i][0:idx]].append(phone_book[i])
```
> 만약 테이블이 있을 경우 해당 테이블의 값과 배열의 값의 앞부분이 같은 지 비교 후 같을 시 false리턴 전부 아닐 시 테이블에 배열의 값을 추가 이를 배열의 크기만큼 반복하면서 한 번도 같지 않을 시 true를 리턴한다.

## 프로그래머스에서 가장 좋아요를 많이 받은 코드
속도 125ms(프로그래머스 예제 가장 느린 기준)
```Python
def solution(phoneBook):
    phoneBook.sort()
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
```
> string타입 정렬 시 글자 + 길이로 정렬되는 것을 이용하여 현재 배열 값과 다음 배열값을 비교하여 true, false를 구하는 방식

정렬 예)

["10", "432", "11", "123", "100", "222", "23"]

["10", "100", "11", "123", "222", "23", "432"]

### 후기
속도 45ms차이로 느리다면 상당히 느리지만, 해시 문제이기에 해시를 사용해서 작성한 것과 스스로 푼 것에 대해 만족한다

하지만 파이썬은 문자열 정렬 시 글자 + 길이로 정렬되어 이런 문제를 풀 때 상당히 유용하다는 점과 for문에 zip을 사용 시 현재와 앞의 배열을 동시에 받아오는 점은 숙지해야하는 점이다.

startwith도 있으나 [0:len()]과 비교해서 속도가 근소하게나마 더 느려서 startwith을 무조건 써야하는 상항이 아니면 쓰지 않을 것 같다
