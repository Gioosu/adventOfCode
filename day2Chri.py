rangeList = []

with open('/Users/chriselleannguillermo/Documents/GitHub/adventOfCode/test.txt', 'r') as f:
    for line in f:
        l = line.split(',')


# ho str a e b. voglio controllare se ripetizioni avvengono nel range da a a b

def findingInvalid(a, b): #funzione che controlla se ci sono ripetizioni consecutive
    found =[]

    for number in range(a, b + 1):
        if consecRipetitions(number):
            found+= consecRipetitions(number)
        
    return set(found)

def consecRipetitions(n): #dato un int n se ci sono ripetizioni all'interno del suo coso
    
    n = str(n)
    foundInvalid = []
    
    for i in range(len(n)//2):
        for j in range(len(n)-i-1):
            if n[j] == n[j+1] and int(n) not in foundInvalid:
                foundInvalid.append(int(n))
    
    return foundInvalid

print(consecRipetitions(7889))

invalidi =[]
total = 0




print(findingInvalid(95, 115))

# PART ONE------------------------
def invalid1(a,b):
    found = []
    
    for number in range(a, b + 1):
        n = str(number)
        cut = len(n)//2
        
        if n[:cut] == n[cut:]:
            found.append(number)
            
    return found

total = 0

for x in l:
    x = x.split('-')
    
    a = int(x[0])
    b = int(x[1])
    
    for y in findingInvalid(a, b):
        total+= y

#print(total)


s = 'ABCABC'



# PART TWO------------------------


def isRepeated(n):
    
    n = str(n)
    
    flag = []

    return 
            
print(isRepeated(123123123))

def invalid2(a,b):
    
    found = []
    
    for number in range(a, b + 1):
        if isRepeated(number) == True:
            found.append(number)

    
    return found

l = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'
l = l.split(',')

total = 0

for x in l:
    x = x.split('-')
    
    a = int(x[0])
    b = int(x[1])
    
    found = invalid2(a, b)
    print(found)
    
    for x in found:
        total+= x

print(total)