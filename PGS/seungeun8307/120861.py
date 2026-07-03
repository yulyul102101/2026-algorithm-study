def solution(keyinput, board):
    x, y= 0, 0
    mx, my = board[0]//2, board[1]//2
    
    for key in keyinput:
        if key == "left" and x > -mx:
            x -= 1
        elif key == "right" and x < mx:
            x += 1
        elif key == "up" and y < my:
            y += 1
        elif key == "down" and y > -my:
            y -= 1
            
    return [x, y]