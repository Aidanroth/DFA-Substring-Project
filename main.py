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
    if len(stateString) <= 4:   # if length is less than equal to 4, cat newChar and return string
        stateString += newChar
        return strToInt(stateString)

    stateString += newChar     # if length is 5, check if a,b,c,d are all present in string
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
    if isa and isb and isc and isd:     # if all chars are present in string
        stateString = stateString[1:]   # removes first char of string
        return strToInt(stateString)

    else:   # if any char is missing at this point, it goes to reject state (aaaaaa == 1365)
        return 1365
        # I'm not 100% that that's what we should be returning, though


def main():

    print(strToInt("dcbad"))
    print(intToStr(1365))
    print(delta("a", "c"))
    print(delta("adcba", "d"))

main()
