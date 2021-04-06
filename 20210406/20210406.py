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
test = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear2"], ["bluesunglasses", "eyewear"],["test", "eyewear"], ["green_turban", "headgear"]]
solution(test)