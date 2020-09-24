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





def main():
    print(strToInt('a'))
    print(strToInt("bd"))
    print(strToInt("dcbad"))




main()