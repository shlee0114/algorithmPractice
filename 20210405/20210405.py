test = ["10", "432", "11", "123", "100", "222", "23"]
test.sort()
print(test)
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
solution(test)