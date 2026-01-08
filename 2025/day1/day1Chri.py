dialPos = 50
result = 0

with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')

        direction = line[0]
        moves = int(line[1:])
        
        for _ in range(moves):
            
            if direction == 'L':
                dialPos -= 1
                
                if dialPos < 0:
                    dialPos = 99 

            else: 
                dialPos += 1

                if dialPos > 99:
                    dialPos = 0 
            
            if dialPos == 0:
                result += 1

print(result)

        


''' #FIRST SOLUTION
result += moves // 100
        moves = moves % 100

        if direction == 'L':
            dialPos-= moves
            if dialPos < 0 :
                dialPos = 100 + dialPos
                result+= 1
                
        else:
            dialPos+= moves
            if dialPos > 99 :
                dialPos = dialPos - 100
                result+= 1
                

        if dialPos == 0:
            result += 1
        
    print(result)
'''

        

        