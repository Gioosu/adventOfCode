'''
--- Day 6: Trash Compactor ---
After helping the Elves in the kitchen, you were taking a break and helping them 
re-enact a movie scene when you over-enthusiastically 
jumped into the garbage chute!

A brief fall later, you find yourself in a garbage smasher. 
Unfortunately, the door's been magnetically sealed.

As you try to find a way out, you are approached by a family of cephalopods! 
They're pretty sure they can get the door open, but it will take some time. 
While you wait, they're curious if you can help the youngest 
cephalopod with her math homework.

Cephalopod math doesn't look that different from normal math. 
The math worksheet (your puzzle input) consists of a list of problems; 
each problem has a group of numbers that need to be either added (+) 
or multiplied (*) together.

However, the problems are arranged a little strangely; 
they seem to be presented next to each other in a very long horizontal list. 
For example:

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
Each problem's numbers are arranged vertically; 
at the bottom of the problem is the symbol for the operation that 
needs to be performed. Problems are separated by a full column of only spaces. 
The left/right alignment of numbers within each problem can be ignored.

So, this worksheet contains four problems:

123 * 45 * 6 = 33210
328 + 64 + 98 = 490
51 * 387 * 215 = 4243455
64 + 23 + 314 = 401
To check their work, cephalopod students are given the grand total of adding 
together all of the answers to the individual problems. In this worksheet, the 
grand total is 33210 + 490 + 4243455 + 401 = 4277556.

Of course, the actual worksheet is much wider. You'll need to make sure to 
unroll it completely so that you can read the problems clearly.

Solve the problems on the math worksheet. What is the grand total found by 
adding together all of the answers to the individual problems?
'''
def mySum(v1, v2):
    result = ""
    rest = 0
    l1, l2 = len(v1), len(v2)
    v1, v2 = v1[::-1], v2[::-1]
    maxLen = max(l1, l2)

    for i in range(maxLen):
        digit1 = int(v1[i]) if i < l1 else 0
        digit2 = int(v2[i]) if i < l2 else 0

        total = digit1 + digit2 + rest
        
        result_digit = total % 10
        rest = total // 10

        result = result + str(result_digit)
    
    if rest > 0:
        result = result + str(rest)

    return result[::-1]

def myMul(v1, v2):
    result = "0"

    if v1 == "0" or v2 == "0":
        return result
    
    if v1 == "1":
        return v2
    
    if v2 == "1":
        return v1

    l1, l2 = len(v1), len(v2)
    v1 = v1[::-1]

    for i in range(l1):
        digit1 = int(v1[i])

        val = ''
        rest = 0
        for j in range(l2):
            digit2 = int(v2[l2 - j - 1])

            prod = digit1 * digit2

            total = prod + rest
            val = val + str(total % 10)
            rest = total // 10
        
        while rest > 0:
            val = val + str(rest % 10)
            rest = rest // 10

        val = val[::-1]
        zeroFill = val + '0'*(i)
        result = mySum(result, zeroFill)

    return result

def part1(numbers, operation):
    length = len(numbers[0])
    result = "0"

    for i in range(length):
        sign = operation[i]
        
        if sign == '*':
            value = "1"
        else:
            value = "0"

        for j in numbers:
            if sign == '*':
                value = myMul(value, str(j[i]))
                
            else:
                value = mySum(value, str(j[i]))
        
        result = mySum(result, value)

    print(result)

'''
--- Part Two ---
The big cephalopods come back to check on how things are going. When they see 
that your grand total doesn't match the one expected by the worksheet, they 
realize they forgot to explain how to read cephalopod math.

Cephalopod math is written right-to-left in columns. Each number is given in 
its own column, with the most significant digit at the top and the least 
significant digit at the bottom. (Problems are still separated with a column 
consisting only of spaces, and the symbol at the bottom of the problem is 
still the operator to use.)

Here's the example worksheet again:

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
Reading the problems right-to-left one column at a time, the problems are 
now quite different:

The rightmost problem is 4 + 431 + 623 = 1058
The second problem from the right is 175 * 581 * 32 = 3253600
The third problem from the right is 8 + 248 + 369 = 625
Finally, the leftmost problem is 356 * 24 * 1 = 8544
Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.

Solve the problems on the math worksheet again. What is the grand total 
found by adding together all of the answers to the individual problems?
'''
def part2(rows, operation):
    # Set the padding to the same size
    max_w = max(len(r) for r in rows)
    padded_rows = [r.ljust(max_w) for r in rows]
    
    # Find the divider (row columns)
    has_content = [False] * max_w
    for r in padded_rows:
        for i, char in enumerate(r):
            if char != ' ':
                has_content[i] = True

    blocks = []
    start = None
    for i in range(max_w):
        if has_content[i] and start is None:
            start = i
        elif not has_content[i] and start is not None:
            blocks.append((start, i))
            start = None
    if start is not None: blocks.append((start, max_w))

    final_grand_total = "0"

    # iter the blocks
    for idx, (s, e) in enumerate(blocks):
        op = operations[idx]
        vertical_numbers = []
        
        # We move from col s to col e
        for col_idx in range(s, e):
            col_str = ""
            for row in padded_rows:
                char = row[col_idx]
                if char != ' ':
                    col_str += char
            
            if col_str:
                vertical_numbers.append(col_str)
        
        if not vertical_numbers:
            continue
            
        block_result = "1" if op == '*' else "0"
        
        for num in vertical_numbers:
            if op == '*':
                block_result = myMul(block_result, num)
            else:
                block_result = mySum(block_result, num)
        
        print("Block", idx+1, op, ": Columns Number", vertical_numbers, 
              "-> Result: "+ block_result)
        final_grand_total = mySum(final_grand_total, block_result)

    print("\nRESULT:", final_grand_total)

### Main starts here ###
part = 2
rows = []
numbersTemp = []

if part == 1:
    with open('./2025/day6/test.txt', 'r') as f:
        for line in f:
            rows.append(line.strip())

        for row in rows:
            tokens = row.split()
            
            if not tokens:
                continue

            isOperatorRow = tokens[0] in ('*', '+')

            if isOperatorRow:
                numbersTemp.append(tokens)
            else:
                numbersTemp.append([str(t) for t in tokens])
                
    operation = numbersTemp.pop()
    row1 = numbersTemp[0]
    row2 = numbersTemp[1]
    row3 = numbersTemp[2]
    numbers = numbersTemp
    part1(numbers, operation)

else:
    filename = './2025/day6/input.txt'

    with open(filename, 'r') as f:
        all_lines = [line.rstrip('\n') for line in f if line.strip()]

    # gets the operations
    op_line = all_lines.pop()
    operations = op_line.split()

    part2(all_lines, operations)