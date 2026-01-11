'''
--- Day 10: Factory ---
Just across the hall, you find a large factory. Fortunately, the Elves here have
plenty of time to decorate. Unfortunately, it's because the factory machines are
all offline, and none of the Elves can figure out the initialization procedure.

The Elves do have the manual for the machines, but the section detailing the
initialization procedure was eaten by a Shiba Inu. All that remains of the
manual are some indicator light diagrams, button wiring schematics, and joltage
requirements for each machine.

For example:

[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
The manual describes one machine per line. Each line contains a single indicator
light diagram in [square brackets], one or more button wiring schematics in
(parentheses), and joltage requirements in {curly braces}.

To start a machine, its indicator lights must match those shown in the diagram,
where . means off and # means on. The machine has the number of indicator lights
shown, but its indicator lights are all initially off.

So, an indicator light diagram like [.##.] means that the machine has four
indicator lights which are initially off and that the goal is to simultaneously
configure the first light to be off, the second light to be on, the third to be on,
and the fourth to be off.

You can toggle the state of indicator lights by pushing any of the listed
buttons. Each button lists which indicator lights it toggles, where 0 means
the first light, 1 means the second light, and so on. When you push a button,
each listed indicator light either turns on (if it was off) or turns off
(if it was on). You have to push each button an integer number of times;
there's no such thing as "0.5 presses" (nor can you push a button a negative
number of times).

So, a button wiring schematic like (0,3,4) means that each time you push that
button, the first, fourth, and fifth indicator lights would all toggle between
on and off. If the indicator lights were [#.....], pushing the button would
change them to be [...##.] instead.

Because none of the machines are running, the joltage requirements are
irrelevant and can be safely ignored.

You can push each button as many times as you like. However, to save on time,
you will need to determine the fewest total presses required to correctly
configure all indicator lights for all machines in your list.

There are a few ways to correctly configure the first machine:

[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
You could press the first three buttons once each, a total of 3 button presses.
You could press (1,3) once, (2,3) once, and (0,1) twice, a total
of 4 button presses.
You could press all of the buttons except (1,3) once each, a total
of 5 button presses.
However, the fewest button presses required is 2. One way to do this
is by pressing the last two buttons ((0,2) and (0,1)) once each.

The second machine can be configured with as few as 3 button presses:

[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
One way to achieve this is by pressing the last three buttons ((0,4),
(0,1,2), and (1,2,3,4)) once each.

The third machine has a total of six indicator lights that need to be
configured correctly:

[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
The fewest presses required to correctly configure it is 2; one way to do
this is by pressing buttons (0,3,4) and (0,1,2,4,5) once each.

So, the fewest button presses required to correctly configure the indicator
lights on all of the machines is 2 + 3 + 2 = 7.

Analyze each machine's indicator light diagram and button wiring schematics.
What is the fewest button presses required to correctly configure the indicator
lights on all of the machines?
'''
def part1(allLights, allButtons):
    result = 0

    # iter the rows
    for i in range(len(allButtons)):
        # gets the lists for the correct row
        buttons = allButtons[i]
        lights = allLights[i]

        # iter all number of press from lowest to highest
        for nPress in range(1, len(buttons) + 1):
            initialState = [False for _ in range(len(lights))]

            # call the recursive function
            if resolvePress1(nPress, initialState, lights, buttons, 0) == True:
                print(nPress, "are enough for row", i + 1)
                result += nPress
                break
    
    print(result)
    
# pressLeft: how many buttons we can still press for our solution
# currenState: the state we actually are in
# result: the final state we want to reach
# buttons: list of buttons
# index: the index from we can use buttons from
def resolvePress1(pressLeft, currentState, result, buttons, index):
    # default case
    # if we have no pressLeft we check if the currentState is the one we want
    if pressLeft == 0:
        return currentState == result
    
    # iter the buttons from index to last
    for i in range(index, len(buttons)):
        # press the button
        nextState = press1(currentState, buttons[i])
    
        # recursive call pressLeft - 1 and + 1 to index because we pressed one
        if resolvePress1(pressLeft - 1, nextState, result, buttons, i + 1):
            return True
    
    return False

# function to press a button and switch the lights connected to it
def press1(state, button):
    # make a new copy
    newState = list(state)

    # iter the lights that button activate
    for i in button:
        newState[i] = not newState[i]

    return newState

'''
--- Part Two ---
All of the machines are starting to come online! Now, it's time to worry about 
the joltage requirements.

Each machine needs to be configured to exactly the specified joltage levels to 
function properly. Below the buttons on each machine is a big lever that you can
use to switch the buttons from configuring the indicator lights to increasing
the joltage levels. (Ignore the indicator light diagrams.)

The machines each have a set of numeric counters tracking its joltage levels,
one counter per joltage requirement. The counters are all initially set to zero.

So, joltage requirements like {3,5,4,7} mean that the machine has four counters
which are initially 0 and that the goal is to simultaneously configure the first
counter to be 3, the second counter to be 5, the third to be 4, and the fourth
to be 7.

The button wiring schematics are still relevant: in this new joltage
configuration mode, each button now indicates which counters it affects,
where 0 means the first counter, 1 means the second counter, and so on.
When you push a button, each listed counter is increased by 1.

So, a button wiring schematic like (1,3) means that each time you push that
button, the second and fourth counters would each increase by 1. If the current
joltage levels were {0,1,2,3}, pushing the button would
change them to be {0,2,2,4}.

You can push each button as many times as you like. However, your finger is
getting sore from all the button pushing, and so you will need to determine
the fewest total presses required to correctly configure each machine's joltage
level counters to match the specified joltage requirements.

Consider again the example from before:

[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
Configuring the first machine's counters requires a minimum of 10 button
presses.One way to do this is by pressing (3) once, (1,3) three times,
(2,3) three times, (0,2) once, and (0,1) twice.

Configuring the second machine's counters requires a minimum of 12 button
presses. One way to do this is by pressing (0,2,3,4) twice, (2,3) five times,
and (0,1,2) five times.

Configuring the third machine's counters requires a minimum of 11 button
presses. One way to do this is by pressing (0,1,2,3,4) five times,
(0,1,2,4,5) five times, and (1,2) once.

So, the fewest button presses required to correctly configure the joltage
level counters on all of the machines is 10 + 12 + 11 = 33.

Analyze each machine's joltage requirements and button wiring schematics.
What is the fewest button presses required to correctly configure the
joltage level counters on all of the machines?
'''
def resolvePress2(index, voltNow, voltRes, buttons, memo):
    stateKey = (index, tuple(voltNow))
    if stateKey in memo:
        return memo[stateKey]
    
    # default case
    # we found the best nPress for each button
    if index == len(buttons):
        if voltNow == voltRes:
            return True, 0
        return False, float('inf')
    
    maxPress = 50
    if not buttons[index]:
        maxPress = 0
    else:
        for i in buttons[index]:
            limit = voltRes[i] - voltNow[i]
            maxPress = min(maxPress, limit)
    
    best = float('inf')
    foundAny = False

    for nPress in range(0, maxPress + 1):
        nextVolt = list(voltNow)
        for i in buttons[index]:
            nextVolt[i] += nPress

        found, totPress = resolvePress2(index + 1, nextVolt, voltRes, buttons, memo)

        if found:
            foundAny = True
            current_sol = totPress + nPress
            if current_sol < best:
                best = current_sol
    
    # Salviamo il risultato nella memo prima di restituirlo
    memo[stateKey] = (foundAny, best)
    return foundAny, best

def part2(allButtons, allEnergy):
    result = 0

    # iter the rows
    for i in range(len(allButtons)):
        # gets the lists for the correct row
        buttons = allButtons[i]
        energies = allEnergy[i]
        initialVolt =  [0 for _ in range(len(energies))]

        # call the recursive function
        memo = {}
        found, totPress = resolvePress2(0, initialVolt, energies, buttons, memo)

        if found:
            print(totPress, "are enough for row", i + 1)
            result += totPress
        else:
            print("❌ Riga", i + 1, "sembra impossibile.")
    
    print(result)

part = 2
lights = []
buttons = []
energy = []

with open('./2025/day10/test.txt', 'r') as f:
    for line in f:
        newLine = line.strip()

        # gets the lights
        temp = [x for x in [newLine.split("[")[1].split("]")[0]]]
        light = []
        for char in temp[0]:
            light += [char == '#']        
        lights += [light]    
    
        # gets the buttons
        temp = [x for x in [newLine.split("] ")[1].split(" {")[0].split(" ")]]
        temp = [
            [tuple(int(n) for n in x.strip("()").split(",") if n) for x in sublist]
            for sublist in temp
        ]

        temp = [[list(x) if isinstance(x, tuple) else [x] for x in sublist] for sublist in temp]
        buttons += temp
        
        # gets energies
        temp = [int(x) for x in newLine.split(" {")[1].split("}")[0].split(",")]
        energy += [temp]

if part == 1:
    part1(lights, buttons)

else:
    part2(buttons, energy)