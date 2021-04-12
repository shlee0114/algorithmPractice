import math
change = False

def changeVal(scoville, fir, snd) :
    tmp = scoville[fir]
    scoville[fir] = scoville[snd]
    scoville[snd] = tmp


def compare(scoville, center):
    global change
    change = False
    left = center * 2 + 1
    right = center* 2 + 2
    if len(scoville) <= left :
        return 
    if scoville[center] > scoville[left] : 
        changeVal(scoville, center, left)
        change = True
    if len(scoville) <= right :
        return 
    if scoville[center] > scoville[right] : 
        changeVal(scoville, center, right)
        change = True

def sortHeap(scoville) :
    index_num = len(scoville)//2
    for i in range(int(index_num)) :
        compare(scoville, i)
        if i > 0 and change:
            for j in range(i, 0, -2) :
                compare(scoville, j/2)

def deleteHeap(scoville) :
    
    value = scoville[0]
    deleNum = 0
    scoville[0] = scoville[len(scoville) - 1]
    del scoville[len(scoville) - 1]
    for i in scoville :
        left = deleNum * 2 + 1
        right = deleNum * 2 + 2
        if left >= len(scoville) :
            return value
        if right >= len(scoville) :
            if scoville[left] < scoville[deleNum] :
                changeVal(scoville, deleNum, left)
                return value
        else :
            if scoville[left] > scoville[right] :
                if scoville[deleNum] > scoville[right] :
                    changeVal(scoville, deleNum, right)
                    deleNum = right
                else :
                    return value
            else :
                if scoville[deleNum] > scoville[left] :
                    changeVal(scoville, deleNum, left)
                    deleNum = left
                else :
                    return value
    
    return value

def addHeap(scoville, item) :
    itemLoc = len(scoville)
    scoville.append(item) 
    for i in range(itemLoc):
        before = itemLoc
        itemLoc = int(math.ceil(itemLoc/2)) - 1
        if itemLoc <= 0:
            itemLoc = 0
        if before == 0 :
            return
        if item < scoville[itemLoc]:
            changeVal(scoville, itemLoc, before)
        else :
            return

def solution(scoville, k):
    global change
    maxVal = max(scoville)
    count = 0
    sortHeap(scoville)
    while scoville[0] < k :
        if len(scoville) == 1:
            return -1
        value = 0
        firstVal = deleteHeap(scoville)
        secondVal = deleteHeap(scoville)
        value = firstVal + (secondVal * 2)
        addHeap(scoville, value)
        count += 1
    return count
print(solution([1,2,3], 11))