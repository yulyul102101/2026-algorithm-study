def solution(players, callings):
    pos = {player: i for i, player in enumerate(players)}
    
    for p in callings:
        i = pos[p]
        front = players[i-1]
        
        players[i], players[i-1] = players[i-1], players[i]
        
        pos[p] = i-1
        pos[front] = i
        
    return players