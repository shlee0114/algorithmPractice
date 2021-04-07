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