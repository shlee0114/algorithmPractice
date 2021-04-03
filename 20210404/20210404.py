dic = {}
def setHash(hashVal):
    for charStr in hashVal:
        if charStr in dic :
            dic[charStr] = dic[charStr]+1
        else :
            dic[charStr] = 1

def checkHash(hashVal):
    returnStr = ""
    for charStr in hashVal:
        if charStr in dic :
            dic[charStr] = dic[charStr]-1

    for test in dic:
        if dic[test] > 0:
            return test
    return returnStr

def solution(participant, completion):
    setHash(participant)
    
    answer = checkHash(completion)
    return answer