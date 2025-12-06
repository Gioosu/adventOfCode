result = 0

with open('./2025/day2/input.txt', 'r') as f:
    line = f.readline()

ranges = line.split(",")

for range in ranges:
    left, right = range.split("-")
    left, right = int(left), int(right)

    while left < right:
        string = str(left)

        if len(string) % 2 == 1:            
            string = '0' + string

        length = len(string)
        half = length // 2

        if string[: half] == string [half :]:
            #print(string)
            result += 1

        left += 1


print("Result = ", result)
        