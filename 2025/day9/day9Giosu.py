'''
--- Day 9: Movie Theater ---
You slide down the firepole in the corner of the playground and land in the 
North Pole base movie theater!

The movie theater has a big tile floor with an interesting pattern. 
Elves here are redecorating the theater by switching out some of the square 
tiles in the big grid they form. Some of the tiles are red; the Elves would 
like to find the largest rectangle that uses red tiles for two of its opposite 
corners. They even have a list of where the red tiles are located in the grid 
(your puzzle input).

For example:

7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
Showing red tiles as # and other tiles as ., the above arrangement of red 
tiles would look like this:

..............
.......#...#..
..............
..#....#......
..............
..#......#....
..............
.........#.#..
..............
You can choose any two red tiles as the opposite corners of your rectangle; 
your goal is to find the largest rectangle possible.

For example, you could make a rectangle (shown as O) with an area of 24 
between 2,5 and 9,7:

..............
.......#...#..
..............
..#....#......
..............
..OOOOOOOO....
..OOOOOOOO....
..OOOOOOOO.#..
..............
Or, you could make a rectangle with area 35 between 7,1 and 11,7:

..............
.......OOOOO..
.......OOOOO..
..#....OOOOO..
.......OOOOO..
..#....OOOOO..
.......OOOOO..
.......OOOOO..
..............
You could even make a thin rectangle with an area of only 6 between 7,3 and 2,3:

..............
.......#...#..
..............
..OOOOOO......
..............
..#......#....
..............
.........#.#..
..............
Ultimately, the largest rectangle you can make in this example has area 50. 
One way to do this is between 2,5 and 11,1:

..............
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..............
.........#.#..
..............
Using two red tiles as opposite corners, what is the largest area of any 
rectangle you can make?
'''
def getArea(t1, t2):
    h = abs(t1[0] - t2[0]) + 1
    w = abs(t1[1] - t2[1]) + 1
    return h * w

def part1(tiles):
    result = 0

    # iter tiles in couples
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            # calculate area
            t1, t2 = tiles[i], tiles[j]
            area = getArea(t1, t2)

            # check if it's better than the best yet
            if area > result:
                result = area

    print(result)

'''
--- Part Two ---
The Elves just remembered: they can only switch out tiles that are red or green.
So, your rectangle can only include red or green tiles.

In your list, every red tile is connected to the red tile before and after it
by a straight line of green tiles. The list wraps, so the first red tile is also
connected to the last red tile. Tiles that are adjacent in your list will always
be on either the same row or the same column.

Using the same example as before, the tiles marked X would be green:

..............
.......#XXX#..
.......X...X..
..#XXXX#...X..
..X........X..
..#XXXXXX#.X..
.........X.X..
.........#X#..
..............
In addition, all of the tiles inside this loop of red and green tiles are also
green. So, in this example, these are the green tiles:

..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............
The remaining tiles are never red nor green.

The rectangle you choose still must have red tiles in opposite corners,
but any other tiles it includes must now be red or green.
This significantly limits your options.

For example, you could make a rectangle out of red and green tiles with an area
of 15 between 7,3 and 11,1:

..............
.......OOOOO..
.......OOOOO..
..#XXXXOOOOO..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............
Or, you could make a thin rectangle with an area of 3 between 9,7 and 9,5:

..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXXOXX..
.........OXX..
.........OX#..
..............
The largest rectangle you can make in this example using only red and green
tiles has area 24. One way to do this is between 9,5 and 2,3:

..............
.......#XXX#..
.......XXXXX..
..OOOOOOOOXX..
..OOOOOOOOXX..
..OOOOOOOOXX..
.........XXX..
.........#X#..
..............
Using two red tiles as opposite corners, what is the largest area of any
rectangle you can make using only red and green tiles?
'''
def part2(tiles):
    valid = set()
    prev = [tiles[len(tiles) - 1][0], tiles[len(tiles) - 1][1]]
    for x, y in tiles:
        minX, maxX = min(x, prev[0]), max(x, prev[0])
        minY, maxY = min(y, prev[1]), max(y, prev[1])
        for i in range(minX, maxX + 1):
            for j in range(minY, maxY + 1):
                valid.add((i, j))

        prev = [x, y]

    min_x, max_x = min(t[0] for t in tiles), max(t[0] for t in tiles)
    min_y, max_y = min(t[1] for t in tiles), max(t[1] for t in tiles)

    for y in range(min_y, max_y + 1):
        is_inside = False
        for x in range(min_x, max_x + 1):
            if (x, y) in valid:
                if (x, y-1) in valid: 
                    is_inside = not is_inside
            else:
                if is_inside:
                    valid.add((x, y))

    result = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            area = getArea(tiles[i], tiles[j])

            if area > result:
                minX, maxX = min(tiles[i][0], tiles[j][0]), max(tiles[i][0], tiles[j][0])
                minY, maxY = min(tiles[i][1], tiles[j][1]), max(tiles[i][1], tiles[j][1])

                inside = True
                for w in range(minX, maxX + 1):
                    if (w, minY) not in valid or (w, maxY) not in valid:
                        inside = False
                        break
                
                for h in range(minY, maxY + 1):
                    if (minX, h) not in valid or (maxX, h) not in valid:
                        inside = False
                        break
                
                if inside:
                    result = area
    
    print(result)



### Main starts here ###
part = 2
tiles = []

with open('./2025/day9/input.txt', 'r') as f:
    for line in f:
        newLine = line.strip()
        tiles += [[int(x) for x in newLine.split(",")]]

if part == 1:
    part1(tiles)

else:
    part2(tiles)