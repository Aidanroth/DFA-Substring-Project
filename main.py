import math


def strToInt(string):
    intSum = 0
    for i in range(len(string)):
        if string[i] == 'a':
            intSum += pow(4, i)
        elif string[i] == 'b':
            intSum += 2 * pow(4, i)
        elif string[i] == 'c':
            intSum += 3 * pow(4, i)
        elif string[i] == 'd':
            intSum += 4 * pow(4, i)
        else:
            intSum += 0
    return intSum


def intToStr(int):
    newStr = ""
    while int > 0:
        remainder = int % 4
        if remainder == 1 or remainder == 2 or remainder == 3:
            if remainder == 1:
                newStr += "a"
            elif remainder == 2:
                newStr += "b"
            elif remainder == 3:
                newStr += "c"
            else:
                print("Error: invalid remainder value. Exiting")
                quit(1)
            int = (int - remainder) / 4

        elif remainder == 0:
            newStr += "d"
            int = (int - 4) / 4
        else:
            print("Error: invalid remainder value. Exiting")
            quit(2)

    return newStr


def delta(currentState, newChar):
    # This function returns the integer of the state that currentState will go to when newChar is added to it

    stateString = currentState
    if len(stateString) <= 4:  # if length is less than equal to 4, cat newChar and return string
        stateString += newChar
        return strToInt(stateString)

    stateString += newChar  # if length is 5, check if a,b,c,d are all present in string
    isa = isb = isc = isd = False
    for char in stateString:
        if char == 'a':
            isa = True
        elif char == 'b':
            isb = True
        elif char == 'c':
            isc = True
        elif char == 'd':
            isd = True
    if isa and isb and isc and isd:  # if all chars are present in string
        stateString = stateString[1:]  # removes first char of string
        return strToInt(stateString)

    else:  # if any char is missing at this point, it goes to reject state (aaaaaa == 1365)
        return 1365
        # I'm not 100% that that's what we should be returning, though


def count(strLength):
    currentarray = [0 for i in
                 range(1365)]  # number of strings of length k-1 that take us from state i to an accepting state
    nextarrray = [0 for i in
                  range(1365)]  # number of strings of length k that take us from state i to an accepting state

    for elem in range(len(currentarray) - 1):  # initialize all currentarray values except for last to 1
        currentarray[elem] = 1

    for i in range(strLength):
        for state in range(len(currentarray)-1):
            astate = currentarray[delta(intToStr(state), 'a') -1]
            bstate = currentarray[delta(intToStr(state), 'b') -1]
            cstate = currentarray[delta(intToStr(state), 'c') -1]
            dstate = currentarray[delta(intToStr(state), 'd') -1]
            nextarrray[state] = astate + bstate + cstate + dstate
            #nextarrray[state] = (currentarray[delta(intToStr(state), 'a')] + currentarray[delta(intToStr(state), 'b')] +
                                 #currentarray[delta(intToStr(state), 'c')] + currentarray[delta(intToStr(state), 'd')])
            currentarray[state] = nextarrray[state]

    nextidx = 0
    currentidx = 0
    falsecount = 0
    for idx in range(len(nextarrray)):
        if nextarrray[idx] == 1560:
            nextidx = idx
        if currentarray[idx] == 1560:
            currentidx = idx
        if nextarrray[idx] != currentarray[idx]:
            equivalent = False
            falsecount += 1
            falseidx = idx
            falsenext = nextarrray[falseidx]
            falsecurrent = currentarray[falseidx]


    return currentarray[0]


def main():
    print(strToInt("adcba"))
    print(intToStr(1))
    print(delta("adcba", "b"))
    print(delta("adcba", "d"))

    # The array created below holds the values for where each state will go if each possible letter is added to it
    # for example, arr[0][2] shows where state 0 will go if c is added to it. arr[449][1] will show adcba + b
    rows, cols = (1365, 4)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            arr[i][j] = delta(intToStr(i), intToStr(j + 1))
    print(arr)

    print("count function:")
    print(count(6))


main()
