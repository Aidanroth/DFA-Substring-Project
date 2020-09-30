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

def main():

    print(strToInt("dcbad"))
    print(intToStr(1136))

main()
