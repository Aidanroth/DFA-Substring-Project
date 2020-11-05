# Aidan Roth and Christopher Roseberry
class DFA:
    Q = []  # set of all states in DFA
    alphabet = []
    delta = []  # transitions
    startState = 0
    acceptingStates = []

def nextState(currentState, symbol, modValue):
    product = 10 * currentState
    sum = product + symbol
    retval = sum % modValue
    return ((10*currentState) + symbol) % modValue

def MinString(numStates, alphabet, inverseAlpha, state_table, acceptingStates):

    isEmpty = not alphabet
    if isEmpty:
        return "No Solution"
    queue = []
    parent = [0 for i in range(numStates)]
    label = [0 for i in range(numStates)]
    visited = [0 for i in range(numStates)]
    next = 0
    current = 0
    prev = 0
    break_flag = False

    for i in range(len(alphabet)):
        next = state_table[0][alphabet[i]]
        visited[next] = True
        queue.append(next)
        parent[next] = prev
        label[next] = alphabet[i]

    while queue:
        current = queue[0]
        queue.pop(0)
        for i in range(len(alphabet)):
            next = state_table[current][alphabet[i]]
            for j in range(len(acceptingStates)):
                if next == acceptingStates[j]:
                    break_flag = True
                    break
            if break_flag:
                parent[next] = current
                label[next] = alphabet[i]
                break
            elif not visited[next]:
                visited[next] = True
                parent[next] = current
                label[next] = alphabet[i]
                queue.append(next)
        if break_flag:
            break

    if not break_flag:
        return "No Solution"
    else:
        temp_string = output = ""
        while parent[next] != 0:
            temp_string += inverseAlpha[label[next]]
            next = parent[next]
        temp_string += inverseAlpha[label[next]]
        j = len(temp_string) - 1
        while j >= 0:
            output += temp_string[j]
            j -= 1
        return output


def smallestMultiple(k, permitted_digits):

    queue = []
    visited = [False for i in range(k)]
    label = [0 for i in range(k)]
    parent = [0 for i in range(k)]
    Next = 0
    current = 0
    break_flag = False
    for i in permitted_digits:
        Next = nextState(0, i, k)
        visited[Next] = True
        queue.append(Next)
        parent[Next] = 0
        label[Next] = i

    while queue:
        placeholder = 5
        current = queue[0]
        queue.pop(0)
        for i in permitted_digits:
            Next = nextState(current, i, k)
            if Next == 0:
                break_flag = True
            if break_flag:
                parent[Next] = current
                label[Next] = i
                break
            elif not visited[Next]:
                visited[Next] = True
                parent[Next] = current
                label[Next] = i
                queue.append(Next)
        if break_flag:
            break

    if not break_flag:
        return "No Solution"
    else:
        temp_string = output = ""
        while parent[Next] != 0:
            temp_string += str(label[Next])
            Next = parent[Next]
        temp_string += str(label[Next])
        j = len(temp_string) -1
        while j >= 0:
            output += temp_string[j]
            j -= 1

        return output

def main():

    k = int(input("Enter value for k, the number of states in the DFA: "))
    dfa = DFA()
    dfa.alphabet = input("\nEnter the permitted numbers separated by spaces : ").strip().split()
    for i in range(len(dfa.alphabet)):
        dfa.alphabet[i] = int(dfa.alphabet[i])

    print("Smallest Multiple: ", smallestMultiple(k, dfa.alphabet))

    symbols = ["a", "b", "c", "d"]
    alphabet_values = [0, 1, 2, 3]
    accepting_states = [4]
    states = [[1, 2, 3, 5], [1, 2, 3, 4], [1, 5, 3, 5], [5, 2, 3, 4], [5, 5, 5, 4], [5, 5, 5, 5]]
    print("The shortest string in the DFA is: ", MinString(len(states), alphabet_values, symbols, states, accepting_states))

    symbols = ["v", "w", "x", "y", "z"]
    alphabet_values.append(4)
    accepting_states = [6]
    states = [[1, 1, 2, 2, 3], [1, 4, 7, 7, 7], [7, 7, 2, 2, 5], [1, 7, 7, 5, 3], [7, 4, 5, 5, 6], [1, 5, 3, 5, 5], [6, 6, 6, 6, 6], [7,7,7,7,7]]
    print("The shortest string in the DFA is: ", MinString(len(states), alphabet_values, symbols, states, accepting_states))

    return


main()