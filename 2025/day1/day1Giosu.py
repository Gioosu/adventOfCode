dialPos = 50
result = 0

def move(dialPos, result, direction, moves):
    print(dialPos)
    result += moves // 100  
    moves = moves % 100
    print(result, moves)

    if direction == 'L':
        if(dialPos - moves < 0):
            moves = moves - dialPos
            dialPos = 100
            result += 1
        if(dialPos == 0):
            result += 1 
        dialPos = dialPos - moves
        print(dialPos)

    else:
        dialPos += moves
        result += dialPos // 100  
        dialPos = dialPos % 100

    return dialPos, result

with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')

        direction = line[0]
        moves = int(line[1:])
        
        print(line)
                   
        dialPos, result = move(dialPos, result, direction, moves)

    print("RESULT: ", result)