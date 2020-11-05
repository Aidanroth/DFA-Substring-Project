# Aidan Roth and Christopher Roseberry

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

    stateString = currentState + newChar

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
    if isa and isb and isc and isd or len(stateString) <= 5:  # if all chars are present in string or length <= 5
        if len(stateString) <= 5:
            return strToInt(stateString)
        else:
            return strToInt(stateString[1:6])

    else:  # if any char is missing at this point, it goes to reject state (aaaaaa == 1365)
        return 1365

def count(strLength):
    prevarray = [1 for i in range(1365)]
    prevarray.append(0)
    currentarray = [0 for i in range(1366)]

    for i in range(strLength):
        for state in range(1366):
            currentarray[state] = (prevarray[delta(intToStr(state), 'a')] + prevarray[delta(intToStr(state), 'b')] +
                                 prevarray[delta(intToStr(state), 'c')] + prevarray[delta(intToStr(state), 'd')])
        for j in range(1366):
            prevarray[j] = currentarray[j]

    return currentarray[0]


def main():
    input_n = int(input("Enter an integer: "))
    answer = count(input_n)
    print("The number of possible strings of length", input_n, "in this DFA is", answer)


main()
