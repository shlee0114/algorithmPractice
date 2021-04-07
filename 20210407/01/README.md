# 프로그래머스 베스트 앨범
**내 코드**
```Python
music = {}
musicCnt = {}
def solution(genres, plays):
    for i in range(len(genres)) :
        if music.get(genres[i]) == None :
            music[genres[i]] = []
            music[genres[i]].append([genres[i], plays[i], i])
            musicCnt[genres[i]] = plays[i]
        else :
            music[genres[i]].append([genres[i], plays[i], i])
            musicCnt[genres[i]] += plays[i]
    for i in music: 
        music[i].sort(key=lambda x:(-x[1], x[2]))
    tmp = sorted(musicCnt.items(), key=lambda x : -x[1])
    answer = []
    for i in tmp :
        answer.append(music[i[0]][0][2])
        if len(music[i[0]]) > 1 :
            answer.append(music[i[0]][1][2])
    return answer
```

>코드 설명
```Python
    for i in range(len(genres)) :
        if music.get(genres[i]) == None :
            music[genres[i]] = []
            music[genres[i]].append([genres[i], plays[i], i])
            musicCnt[genres[i]] = plays[i]
        else :
            music[genres[i]].append([genres[i], plays[i], i])
            musicCnt[genres[i]] += plays[i]
```
> genres에 2개의 정보가 들어오는데 하나는 종류와 해당 종류의 재생 수가 들어온다. 해당 종류가 없다면 생성하고 있다면 추가하는 방식이다.
>> musicCnt는 해당 장르의 총 합이다.

```Python
    for i in music: 
        music[i].sort(key=lambda x:(-x[1], x[2]))
    tmp = sorted(musicCnt.items(), key=lambda x : -x[1])
```
> 저장한 값을 정렬한다. music은 내부의 장르별 값만 정렬을 하고 musicCnt는 전체 정렬을 돌린다.
>>내림차순으로 정렬한다.
```Python
    for i in tmp :
        answer.append(music[i[0]][0][2])
        if len(music[i[0]]) > 1 :
            answer.append(music[i[0]][1][2])
```
> 장르별로 정렬한 것을 토대로 장르순, 해당 장르내의 재생 수로 2개만 뽑아서 저장한다. 하나만 있을 경우도 있어서 예외처리를 진행했다.

## 프로그래머스에서 추천수가 가장 높은 코드

```Python
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer
```

### ***개인적 분석***

```Python
    d = {e:[] for e in set(genres)}
```

>id만 추출해서 테이블의 키 값으로 미리 선언

```Python
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
```

> 상위에서 선언된 테이블에 재생 수와 고유번호를 입력한다.

```Python
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
```

> list(d.keys())는 내부 람다식 y의 인자가 되어서 해당 키의 총합을 내부 람다에서 구한 후 해당 값으로 내림차순으로 정렬

```Python
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
```

> 장르의 수만큼 돌면서 장르의 명을 키 값으로 가지고 있는 인자들을 재생수와 고유번호로 정렬을 한 다음 고유번호만 따로 빼서 temp에 배열로 저장한 후 자료형의 최소값을 전달하는 min함수와 2를 입력해서 2개만 저장한다.
