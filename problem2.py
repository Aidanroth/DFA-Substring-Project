class DFA:
    Q = []  # set of all states in DFA
    alphabet = []
    delta = []  # transitions
    startState = 0
    acceptingStates = []

def nextState(currentState, symbol, modValue):
    return (10*currentState + symbol) % modValue

def MinString(numStates, dfa):

    queue = []
    parent = [0 for i in range(numStates)]
    label = [0 for i in range(numStates)]
    visited = [0 for i in range(numStates)]
    for j in range(numStates):
        for s in dfa.alphabet:
            next = nextState(0, s, numStates)
            visited[next] = 1
            queue.append(next)
            parent[next] = 0
            label[next] = s
        while queue:
            curr = queue.pop()
            for s in dfa.alphabet:
                next = nextState(curr, s, numStates)
                if next == 0:
                    parent[next] = curr
                    label[next] = s
                    break
                elif visited[next] is None:
                    visited[next] = True
                    parent[next] = curr
                    label[next] = s  # pseudocode says label[next] = c in pseudocode, but c was not mentioned previously
                    queue.append(next)
    if next != 0:  # pseudocode says if(next != 0), but next hasn't been defined in this scope
        print("No solution")
        return ""
    else:
        solution = ""
        #while parent[]





    return


def smallestMultiple():

    return

def main():

    k = int(input("Enter value for k, the number of states in the DFA: "))
    dfa = DFA()
    dfa.alphabet = input("\nEnter the numbers : ").strip().split()
    for i in range(len(dfa.alphabet)):
        dfa.alphabet[i] = int(dfa.alphabet[i])
    MinString(k, dfa)

    print(dfa.alphabet)

    return


main()