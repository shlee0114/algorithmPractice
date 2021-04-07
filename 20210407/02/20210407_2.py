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