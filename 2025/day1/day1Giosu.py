dialPos = 50
result = 0

def move(dialPos, result, direction, moves):
    #print("START      -> dial: ", dialPos, "result: ", result, "moves: ", moves)
    result += moves // 100 
    moves = moves % 100

    if direction == 'L': 
        if(dialPos - moves <= 0 and 0 < dialPos):
            result += 1
        
        moves = -1 * moves

    else: 
        if(dialPos < 100 and 100 <= dialPos + moves):
            result += 1
        
    dialPos = (dialPos + moves) % 100
        

    #print("END        -> dial: ", dialPos, "result: ", result, "moves: ", moves)
    return dialPos, result

with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')

        direction = line[0]
        moves = int(line[1:])
        
        #print(line)
                   
        dialPos, result = move(dialPos, result, direction, moves)

    print("RESULT: ", result)