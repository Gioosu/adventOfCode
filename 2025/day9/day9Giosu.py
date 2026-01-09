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
    # function to find if coords are inside or outside the square
    def is_inside(x, y):
        size = len(tiles)
        inside = False
        p1x, p1y = tiles[0]

        # iter the tiles
        for i in range(size + 1):
            # % size to connect last to first
            p2x, p2y = tiles[i % size]
            if x == p1x == p2x and min(p1y, p2y) <= y <= max(p1y, p2y): return True
            if y == p1y == p2y and min(p1x, p2x) <= x <= max(p1x, p2x): return True
            
            # had to use google to study something about raycasting
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            # calc the straight line passing through the points
                            xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        # vertical or left
                        if p1x == p2x or x <= xints:
                            inside = not inside
            # update previous
            p1x, p1y = p2x, p2y
        return inside

    # find all segments connecting the edges
    segments = []
    for i in range(len(tiles)):
        p1 = tiles[i]
        p2 = tiles[(i + 1) % len(tiles)]
        segments.append((p1, p2))

    # check if all corners are inside
    def is_rect_valid(x1, y1, x2, y2):
        corners = [(x1, y1), (x2, y1), (x1, y2), (x2, y2)]
        for cx, cy in corners:
            if not is_inside(cx, cy):
                return False
        
        # check if any segments of the "red" polygon goes through our rectangle
        # we are working just with horizontal or vertical so we just check
        # if it cuts the segments in half
        for p1, p2 in segments:
            # vertical segments
            if p1[0] == p2[0]:
                sx = p1[0]
                sy_min, sy_max = min(p1[1], p2[1]), max(p1[1], p2[1])
                if x1 < sx < x2: # segment cuts off a vertical border
                    if not (sy_max <= y1 or sy_min >= y2):
                        return False
            # horizontal segments
            else:
                sy = p1[1]
                sx_min, sx_max = min(p1[0], p2[0]), max(p1[0], p2[0])
                if y1 < sy < y2:
                    if not (sx_max <= x1 or sx_min >= x2):
                        return False
        return True

    max_area = 0
    # find the best
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            
            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)
            
            area = getArea(tiles[i], tiles[j])
            if area <= max_area:
                continue
            
            if is_rect_valid(min_x, min_y, max_x, max_y):
                max_area = area

    print(max_area)

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