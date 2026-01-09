'''
--- Day 8: Playground ---
Equipped with a new understanding of teleporter maintenance, you confidently 
step onto the repaired teleporter pad.

You rematerialize on an unfamiliar teleporter pad and find yourself in a vast 
underground space which contains a giant playground!

Across the playground, a group of Elves are working on setting up an ambitious 
Christmas decoration project. Through careful rigging, they have suspended 
a large number of small electrical junction boxes.

Their plan is to connect the junction boxes with long strings of lights. 
Most of the junction boxes don't provide electricity; however, when two 
junction boxes are connected by a string of lights, electricity can pass 
between those two junction boxes.

The Elves are trying to figure out which junction boxes to connect so 
that electricity can reach every junction box. They even have a list 
of all of the junction boxes' positions in 3D space (your puzzle input).

For example:

162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
This list describes the position of 20 junction boxes, one per line. 
Each position is given as X,Y,Z coordinates. So, the first junction box 
in the list is at X=162, Y=817, Z=812.

To save on string lights, the Elves would like to focus on connecting 
pairs of junction boxes that are as close together as possible according 
to straight-line distance. In this example, the two junction boxes which 
are closest together are 162,817,812 and 425,690,689.

By connecting these two junction boxes together, because electricity can 
flow between them, they become part of the same circuit. After connecting 
them, there is a single circuit which contains two junction boxes, and the 
remaining 18 junction boxes remain in their own individual circuits.

Now, the two junction boxes which are closest together but aren't already 
directly connected are 162,817,812 and 431,825,988. After connecting them, 
since 162,817,812 is already connected to another junction box, there is now a 
single circuit which contains three junction boxes and an additional 17 circuits
which contain one junction box each.

The next two junction boxes to connect are 906,360,560 and 805,96,715.
After connecting them, there is a circuit containing 3 junction boxes,
a circuit containing 2 junction boxes, and 15 circuits which contain one
junction box each.

The next two junction boxes are 431,825,988 and 425,690,689. Because these two
junction boxes were already in the same circuit, nothing happens!

This process continues for a while, and the Elves are concerned that they
don't have enough extension cables for all these circuits. They would like to
know how big the circuits will be.

After making the ten shortest connections, there are 11 circuits: one circuit
which contains 5 junction boxes, one circuit which contains 4 junction boxes,
two circuits which contain 2 junction boxes each, and seven circuits which each
contain a single junction box. Multiplying together the sizes of the three
largest circuits (5, 4, and one of the circuits of size 2) produces 40.

Your list contains many junction boxes; connect together the 1000 pairs of
junction boxes which are closest together. Afterward, what do you get if you
multiply together the sizes of the three largest circuits?
'''
import math as m

# Calcultate 3d Distance
def getDistance(coord1, coord2):
    return m.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2 + (coord2[2] - coord1[2])**2)

# merge unions
def merge(coord1, coord2, union):                
    idx1 = -1
    idx2 = -1

    # find indexes for coords
    for i in range(len(union)):
        if coord1 in union[i]:
            idx1 = i
        if coord2 in union[i]:
            idx2 = i
        
        if idx1 != -1 and idx2 != -1:
            break
    
    # merge them if they are in different sets
    if idx1 != -1 and idx2 != -1 and idx1 != idx2:
        if idx1 > idx2:
            second = union.pop(idx1)
            union[idx2] += second
        else:
            second = union.pop(idx2)
            union[idx1] += second

def part1(coords):
    distances = []
    union = []

    # calculate all distances and put in tuples with coords
    for i in range(len(coords)):
        union += [[coords[i]]]
        for j in range(i + 1, len(coords)):
            distance = getDistance(coords[i], coords[j])
            distances += [(distance, coords[i], coords[j])]
    
    # sort by distance
    distances.sort(key=lambda x: x[0])

    # get the best (10 for test, 1000 for input)
    best = 10
    distances = distances[0:best]

    # merge best distances
    for d in distances:
        merge(d[1], d[2], union)
    
    # make sizes list
    sizes = []
    for u in union:
        sizes += [len(u)]

    # order by desc
    sizes.sort(reverse = True)

    result = 1
    for i in range(3):
        result *= sizes[i]

    print(result)

'''
--- Part Two ---
The Elves were right; they definitely don't have enough extension cables. 
You'll need to keep connecting junction boxes together until they're 
all in one large circuit.

Continuing the above example, the first connection which causes all of the 
junction boxes to form a single circuit is between the junction boxes at 
216,146,977 and 117,168,530. The Elves need to know how far those junction boxes
are from the wall so they can pick the right extension cable; multiplying the X
coordinates of those two junction boxes (216 and 117) produces 25272.

Continue connecting the closest unconnected pairs of junction boxes together
until they're all in the same circuit. What do you get if you multiply together
the X coordinates of the last two junction boxes you need to connect?
'''
def part2(coords):
    distances = []
    union = []

    # calculate all distances and put in tuples with coords
    for i in range(len(coords)):
        union += [[coords[i]]]
        for j in range(i + 1, len(coords)):
            distance = getDistance(coords[i], coords[j])
            distances += [(distance, coords[i], coords[j])]
    
    # sort by distance
    distances.sort(key=lambda x: x[0])

    # merge best distances
    last, secondLast = (), ()
    for d in distances:
        merge(d[1], d[2], union)

        # break when you find the last merge
        if len(union) == 1:
            last = d[1][0]
            secondLast = d[2][0]
            break
    
    print(last, secondLast)
    print(last * secondLast)

### Main starts here ###
part = 2
coords = []

with open('./2025/day8/input.txt', 'r') as f:
    for line in f:
        newLine = [int(n.strip()) for n in line.split(",")]
        coords.append(tuple(int(x) for x in newLine))

if part == 1:
    part1(coords)

else:
    part2(coords)