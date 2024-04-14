#we will use the following function to union two NFAs
def union_NFA(nfa1, nfa2):
    global counter
    new_nfa = create_NFA()
    new_nfa.add_epsilon(nfa1.stateName)
    new_nfa.add_epsilon(nfa2.stateName)
    nfa1.stateName = "S" + str(counter)
    counter += 1
    nfa2.stateName = "S" + str(counter)
    counter += 1
    return new_nfa

#we will use the following function to concatenate two NFAs
def concatenate_NFA(nfa1, nfa2):
    nfa1.add_epsilon(nfa2.stateName)
    nfa1.stateName = nfa2.stateName
    return nfa1

#we will use the following function to apply the kleene star operation on an NFA
def kleene_star_NFA(nfa):
    global counter
    new_nfa = create_NFA()
    new_nfa.add_epsilon(nfa.stateName)
    new_nfa.add_epsilon("S" + str(counter))
    nfa.add_epsilon(nfa.stateName)
    nfa.add_epsilon("S" + str(counter))
    nfa.stateName = "S" + str(counter)
    counter += 1
    return new_nfa

#we will use the following function to apply the one or more operation on an NFA
def one_or_more_NFA(nfa):
    global counter
    new_nfa = create_NFA()
    new_nfa.add_epsilon(nfa.stateName)
    new_nfa.add_epsilon("S" + str(counter))
    nfa.add_epsilon("S" + str(counter))
    nfa.stateName = "S" + str(counter)
    counter += 1
    return new_nfa

#we will use the following function to apply the zero or one operation on an NFA
def zero_or_one_NFA(nfa):
    global counter
    new_nfa = create_NFA()
    new_nfa.add_epsilon(nfa.stateName)
    new_nfa.add_epsilon("S" + str(counter))
    nfa.add_epsilon("S" + str(counter))
    counter += 1
    return new_nfa

def create_symbol_NFA(symbol, isTerminatingState=False):
    global counter
    nfa = create_NFA(isTerminatingState)
    nfa.add_transition(symbol, "S" + str(counter))
    nfa1 = create_NFA()
    nfa1.stateName = "S" + str(counter)
    counter += 1
    return nfa, nfa1

def create_range_NFA(symbol, isTerminatingState=False):
    global counter
    nfa = create_NFA(isTerminatingState)
    nfa.add_transition(symbol, "S" + str(counter))
    nfa1 = create_NFA()
    nfa1.stateName = "S" + str(counter)
    counter += 1
    return nfa, nfa1

#we will use the following function to create a new NFA with a single symbol
def create_dot_NFA(isTerminatingState=False):
    global counter
    nfa = create_NFA(isTerminatingState)
    nfa.add_transition(".", "S" + str(counter))
    nfa1 = create_NFA()
    nfa1.stateName = "S" + str(counter)
    counter += 1
    return nfa, nfa1

#we will use the following function to create a new NFA with a single symbol
def create_epsilon_NFA():
    global counter
    nfa = create_NFA()
    nfa.add_epsilon("S" + str(counter))
    nfa1 = create_NFA()
    nfa1.stateName = "S" + str(counter)
    counter += 1
    return nfa, nfa1

#we will use the following function to union two NFAs
def union_NFA(nfa1, nfa2):
    global counter
    new_nfa = create_NFA()
    new_nfa.add_epsilon(nfa1.stateName)
    new_nfa.add_epsilon(nfa2.stateName)
    nfa1.stateName = "S" + str(counter)
    counter += 1
    nfa2.stateName = "S" + str(counter)
    counter += 1
    return new_nfa

#get the NFA from the postfix notation
def postfix_NFA(postfix, range_list):
    global counter
    stack = []
    for i in postfix:

        if i == len(postfix)-1: #if we reached the last element so it is the terminating state
            nfa = stack.pop()
            nfa.isTerminatingState = True
            stack.append(nfa)

        if i in alphabet_nums + ["#"]:
            if i == "#":
                nfa, nfa1 = create_range_NFA(range_list.pop(0))
                stack.append(nfa)
                stack.append(nfa1)
            elif i == ".":
                nfa, nfa1 = create_dot_NFA()
                stack.append(nfa)
                stack.append(nfa1)
            else:
                nfa, nfa1 = create_symbol_NFA(i)
                stack.append(nfa)
                stack.append(nfa1)
        elif i == "&":
            nfa1 = stack.pop()
            nfa2 = stack.pop()
            nfa = concatenate_NFA(nfa2, nfa1)
            stack.append(nfa)
        elif i == "|":
            nfa1 = stack.pop()
            nfa2 = stack.pop()
            nfa = union_NFA(nfa2, nfa1)
            stack.append(nfa)
        elif i == "*":
            nfa = stack.pop()
            nfa = kleene_star_NFA(nfa)
            stack.append(nfa)
        elif i == "+":
            nfa = stack.pop()
            nfa = one_or_more_NFA(nfa)
            stack.append(nfa)
        elif i == "?":
            nfa = stack.pop()
            nfa = zero_or_one_NFA(nfa)
            stack.append(nfa)
    return stack





########################################

class Node:
    def __init__(self, stateName, isTerminatingState=False):
        self.stateName = stateName
        self.isTerminatingState = isTerminatingState
        self.transitions = {} #dictionary of transitions with the symbol (ex. "a") as the key and the state name as the value
        self.epsilon = [] #list of states that can be reached by epsilon transitions

    def add_transition(self, symbol, stateName):
        self.transitions[symbol] = stateName

    def add_epsilon(self, stateName):
        self.epsilon.append(stateName)

    def __str__(self):
        return f"stateName: {self.stateName}, transitions: {self.transitions}, epsilon: {self.epsilon}, isTerminatingState: {self.isTerminatingState}"
    
    def __repr__(self):
        return f"stateName: {self.stateName}, transitions: {self.transitions}, epsilon: {self.epsilon}, isTerminatingState: {self.isTerminatingState}"
    
#test the Node class
node = Node("S0", False)
node1 = Node("S1", False)
node2 = Node("S2", True)
node.add_transition("a", "S1")
node.add_transition("b", "S0")
node.add_epsilon("S1")
node.add_epsilon("S2")


print(node)

#we will use the following function to create a new NFA
def create_NFA(isTerminatingState=True):
    global counter
    nfa = Node("S" + str(counter), isTerminatingState)
    counter += 1
    return nfa

#Union two NFAs
def union_NFA(nfa1, nfa2):
    #create a new NFA which will go to the starting states of nfa1 and nfa2
    new_nfa = create_NFA(isTerminatingState=False)
    new_nfa.add_epsilon(nfa1.stateName)
    new_nfa.add_epsilon(nfa2.stateName)
    nfa1.isTerminatingState = False #make the terminating state of nfa1 a non-terminating state
    nfa2.isTerminatingState = False #make the terminating state of nfa2 a non-terminating state
    #create a new NFA which will be the new terminating state
    new_nfa1 = create_NFA()
    nfa1.add_epsilon(new_nfa1.stateName)
    nfa2.add_epsilon(new_nfa1.stateName)
    return new_nfa, new_nfa1

#Concatenate two NFAs
def concatenate_NFA(nfa1, nfa2):
    nfa1.isTerminatingState = False #make the terminating state of nfa1 a non-terminating state
    nfa1.add_epsilon(nfa2.stateName)
    return nfa1

#Apply the kleene star operation on an NFA
def kleene_star_NFA(nfa):
    #create a new NFA which will go to the starting state of nfa
    new_nfa = create_NFA()
    new_nfa.add_epsilon(nfa.stateName)
    nfa.isTerminatingState = False #make the terminating state of nfa a non-terminating state
    nfa.add_epsilon(new_nfa.stateName)
    nfa.add_epsilon(nfa.stateName)
    return new_nfa, new_nfa

#Apply the one or more operation on an NFA
def one_or_more_NFA(nfa):
    #create a new NFA which will go to the starting state of nfa
    new_nfa = create_NFA() 
    new_nfa.add_epsilon(nfa.stateName)
    nfa.isTerminatingState = False #make the terminating state of nfa a non-terminating state
    nfa.add_epsilon(new_nfa.stateName)
    return nfa, new_nfa

#Apply the zero or one operation on an NFA
def zero_or_one_NFA(nfa):
    #create a new NFA which will go to the starting state of nfa
    new_nfa = create_NFA()
    new_nfa.add_epsilon(nfa.stateName)
    return new_nfa, nfa

#Apply the dot operator on an NFA
def dot_NFA():
    #create a 2 new NFAs, with two states, one is the starting state and the other is the terminating state
    new_nfa = create_NFA(isTerminatingState=False) 
    new_nfa1 = create_NFA()
    new_nfa.add_transition(".", new_nfa1.stateName)
    return new_nfa, new_nfa1

#Apply the range operator on an NFA
def range_NFA(range_list):
    #create a 2 new NFAs, with two states, one is the starting state and the other is the terminating state
    new_nfa = create_NFA(isTerminatingState=False) 
    new_nfa1 = create_NFA()
    new_nfa.add_transition(range_list, new_nfa1.stateName)
    return new_nfa, new_nfa1

#Apply the symbol operator on an NFA
def symbol_NFA(symbol):
    new_nfa = create_NFA(isTerminatingState=False) #create a new NFA with two states, one is the starting state and the other is the terminating state
    new_nfa1 = create_NFA()
    new_nfa.add_transition(symbol, new_nfa1.stateName)
    return new_nfa, new_nfa1

#we will use the following function to construct the NFA from the postfix notation
def postfix_NFA(postfix, range_list):
    stack = []
    #starting state
    new_nfa = create_NFA()
    new_nfa.isTerminatingState = False
    new_nfa.add_epsilon("S1")
    stack.append(new_nfa)

    for i in postfix:
        if i in alphabet_nums:
            nfa, nfa1 = symbol_NFA(i)
            stack.append(nfa)
            stack.append(nfa1)
        elif i == "&":
            nfa2, nfa1 = stack.pop(), stack.pop()
            nfa = concatenate_NFA(nfa1, nfa2)
            stack.append(nfa)
        elif i == "|":
            nfa2, nfa1 = stack.pop(), stack.pop()
            nfa, nfa1 = union_NFA(nfa1, nfa2)
            stack.append(nfa)
            stack.append(nfa1)
        elif i == "*":
            nfa = stack.pop()
            nfa, nfa1 = kleene_star_NFA(nfa)
            stack.append(nfa)
            stack.append(nfa1)
        
        elif i == "+":
            nfa = stack.pop()
            nfa, nfa1 = one_or_more_NFA(nfa)
            stack.append(nfa)
            stack.append(nfa1)
        elif i == "?":
            nfa = stack.pop()
            nfa, nfa1 = zero_or_one_NFA(nfa)
            stack.append(nfa)
            stack.append(nfa1)
        elif i == ".":
            nfa, nfa1 = dot_NFA()
            stack.append(nfa)
            stack.append(nfa1)
        elif i == "#":
            nfa, nfa1 = range_NFA(range_list.pop(0))
            stack.append(nfa)
            stack.append(nfa1)
    return stack


#########################

# Define the constants
EPSILON = 'ε'
alphabet_nums = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [str(i) for i in range(10)]

# Define the class for representing NFA nodes
class Node:
    def __init__(self, stateName, isTerminatingState=False):
        self.stateName = stateName
        self.isTerminatingState = isTerminatingState
        self.transitions = {}
        self.epsilon = []

    def add_transition(self, symbol, stateName):
        self.transitions[symbol] = stateName

    def add_epsilon(self, stateName):
        self.epsilon.append(stateName)

    def __str__(self):
        return f"stateName: {self.stateName}, transitions: {self.transitions}, epsilon: {self.epsilon}, isTerminatingState: {self.isTerminatingState}"
    
    def __repr__(self):
        return f"stateName: {self.stateName}, transitions: {self.transitions}, epsilon: {self.epsilon}, isTerminatingState: {self.isTerminatingState}"

# Define the class for representing NFA
class NFA:
    def __init__(self):
        self.startingState = None
        self.terminatingState = None
        self.states = {}

    def add_state(self, state):
        self.states[state.stateName] = state

    def add_epsilon_transition(self, stateName1, stateName2):
        self.states[stateName1].add_epsilon(stateName2)

    def add_transition(self, stateName1, symbol, stateName2):
        self.states[stateName1].add_transition(symbol, stateName2)

    def __str__(self):
        return f"startingState: {self.startingState}, terminatingState: {self.terminatingState}, states: {self.states}"
    
    def __repr__(self):
        return f"startingState: {self.startingState}, terminatingState: {self.terminatingState}, states: {self.states}"
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
    
    def get_state(self, stateName):
        return self.states[stateName]
    
    def get_states(self):
        return self.states
    
    def get_starting_state(self):
        return self.startingState
    
    def get_terminating_state(self):
        return self.terminatingState
    
    def set_starting_state(self, stateName):
        self.startingState = stateName

    def set_terminating_state(self, stateName):
        self.terminatingState = stateName

# Define the function to create a new NFA
def create_new_NFA(counter):
    nfa = NFA()
    stateName1 = f"S{counter}"
    stateName2 = f"S{counter + 1}"
    nfa.set_starting_state(stateName1)
    nfa.set_terminating_state(stateName2)
    nfa.add_state(Node(stateName1))
    nfa.add_state(Node(stateName2, True))
    return nfa, stateName1, stateName2

# Define the function to union two NFAs
def union_NFAs(nfa1, nfa2, counter):
    nfa = NFA()
    stateName1 = f"S{counter}"
    stateName2 = f"S{counter + 1}"
    nfa.set_starting_state(stateName1)
    nfa.set_terminating_state(stateName2)
    nfa.add_state(Node(stateName1))
    nfa.add_state(Node(stateName2, True))
    nfa.add_epsilon_transition(stateName1, nfa1.get_starting_state())
    nfa.add_epsilon_transition(stateName1, nfa2.get_starting_state())
    nfa.add_epsilon_transition(nfa1.get_terminating_state(), stateName2)
    nfa.add_epsilon_transition(nfa2.get_terminating_state(), stateName2)
    for state in nfa1.get_states().values():
        nfa.add_state(state)
    for state in nfa2.get_states().values():
        nfa.add_state(state)
    return nfa, stateName1, stateName2

# Define the function to concatenate two NFAs
def concatenate_NFAs(nfa1, nfa2):
    nfa = NFA()
    nfa.set_starting_state(nfa1.get_starting_state())
    nfa.set_terminating_state(nfa2.get_terminating_state())
    for state in nfa1.get_states().values():
        nfa.add_state(state)
    for state in nfa2.get_states().values():
        nfa.add_state(state)
    nfa.add_epsilon_transition(nfa1.get_terminating_state(), nfa2.get_starting_state())
    return nfa, nfa1.get_starting_state(), nfa2.get_terminating_state()

# Define the function to apply the kleene star operation on an NFA
def kleene_star_NFA(nfa1, counter):
    nfa = NFA()
    stateName1 = f"S{counter}"
    stateName2 = f"S{counter + 1}"
    nfa.set_starting_state(stateName1)
    nfa.set_terminating_state(stateName2)
    nfa.add_state(Node(stateName1))
    nfa.add_state(Node(stateName2, True))
    nfa.add_epsilon_transition(stateName1, nfa1.get_starting_state())
    nfa.add_epsilon_transition(stateName1, stateName2)
    nfa.add_epsilon_transition(nfa1.get_terminating_state(), nfa1.get_starting_state())
    nfa.add_epsilon_transition(nfa1.get_terminating_state(), stateName2)
    for state in nfa1.get_states().values():
        nfa.add_state(state)
    return nfa, stateName1, stateName2

# Define the function to apply the one or more operation on an NFA
def one_or_more_NFA(nfa1, counter):
    nfa = NFA()
    stateName1 = f"S{counter}"
    stateName2 = f"S{counter + 1}"
    nfa.set_starting_state(stateName1)
    nfa.set_terminating_state(stateName2)
    nfa.add_state(Node(stateName1))
    nfa.add_state(Node(stateName2, True))
    nfa.add_epsilon_transition(stateName1, nfa1.get_starting_state())
    nfa.add_epsilon_transition(nfa1.get_terminating_state(), nfa1.get_starting_state())
    nfa.add_epsilon_transition(nfa1.get_terminating_state(), stateName2)
    for state in nfa1.get_states().values():
        nfa.add_state(state)
    return nfa, stateName1, stateName2

# Define the function to apply the zero or one operation on an NFA
def zero_or_one_NFA(nfa1, counter):
    nfa = NFA()
    stateName1 = f"S{counter}"
    stateName2 = f"S{counter + 1}"
    nfa.set_starting_state(stateName1)
    nfa.set_terminating_state(stateName2)
    nfa.add_state(Node(stateName1))
    nfa.add_state(Node(stateName2, True))
    nfa.add_epsilon_transition(stateName1, nfa1.get_starting_state())
    nfa.add_epsilon_transition(stateName1, stateName2)
    nfa.add_epsilon_transition(nfa1.get_terminating_state(), stateName2)
    for state in nfa1.get_states().values():
        nfa.add_state(state)
    return nfa, stateName1, stateName2

# Define the function to apply the dot operation on an NFA
def dot_NFA(counter):
    nfa = NFA()
    stateName1 = f"S{counter}"
    stateName2 = f"S{counter + 1}"
    nfa.set_starting_state(stateName1)
    nfa.set_terminating_state(stateName2)
    nfa.add_state(Node(stateName1))
    nfa.add_state(Node(stateName2, True))
    nfa.add_transition(stateName1, ".", stateName2)
    return nfa, stateName1, stateName2

# Define the function to apply the range operation on an NFA
def range_NFA(counter, range_list):
    nfa = NFA()
    stateName1 = f"S{counter}"
    stateName2 = f"S{counter + 1}"
    nfa.set_starting_state(stateName1)
    nfa.set_terminating_state(stateName2)
    nfa.add_state(Node(stateName1))
    nfa.add_state(Node(stateName2, True))
    nfa.add_transition(stateName1, range_list[0], stateName2)
    return nfa, stateName1, stateName2

#Change the postfix notation to the required NFA using Thompson's rules
def postfix_NFA(postfix, range_list):
    stack = []
    counter = 0
    for i in postfix:
        if i in alphabet_nums + ["#"]:
            nfa, stateName1, stateName2 = create_new_NFA(counter)
            counter += 2
            stack.append(nfa)
        elif i == "&":
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            nfa, stateName1, stateName2 = concatenate_NFAs(nfa1, nfa2)
            stack.append(nfa)
        elif i == "|":
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            nfa, stateName1, stateName2 = union_NFAs(nfa1, nfa2, counter)
            counter += 2
            stack.append(nfa)
        elif i == "*":
            nfa1 = stack.pop()
            nfa, stateName1, stateName2 = kleene_star_NFA(nfa1, counter)
            counter += 2
            stack.append(nfa)
        elif i == "+":
            nfa1 = stack.pop()
            nfa, stateName1, stateName2 = one_or_more_NFA(nfa1, counter)
            counter += 2
            stack.append(nfa)
        elif i == "?":
            nfa1 = stack.pop()
            nfa, stateName1, stateName2 = zero_or_one_NFA(nfa1, counter)
            counter += 2
            stack.append(nfa)
        elif i == ".":
            nfa, stateName1, stateName2 = dot_NFA(counter)
            counter += 2
            stack.append(nfa)
        elif i == "#":
            nfa, stateName1, stateName2 = range_NFA(counter, range_list)
            counter += 2
            stack.append(nfa)
    return stack.pop()

    


