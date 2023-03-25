class State:
    def __init__(self, l):
        self.pos = l.index(0)
        self.x = self.pos%3
        self.y = self.pos//3
        self.board = l

    def __eq__(self, other):
        if isinstance(other, State):
            return self.board == other.board

    def gen_choices(self): #generate possible move(s)
        choices = []
        if self.x>0: choices.append(('left',-1))
        if self.x<2: choices.append(('right',1))
        if self.y>0: choices.append(('up',-3))
        if self.y<2: choices.append(('down',3))
        return choices
    
    def is_goal(self):
        if self.board==[0,1,2,3,4,5,6,7,8]: return 1
        else: return 0

    def printboard(self):
        print(*[self.board[i] if i%3!=0 or i==0 else '\n'+str(self.board[i]) for i in range(len(self.board))])


def newstate(parent, indx): #child state 
    newboard = parent.board.copy()
    p = parent.pos
    newboard[p],newboard[p+indx] = newboard[p+indx], newboard[p]
    return State(newboard)

def DFS(depth,current): #Depth-first search
        global node_expanded, maxnode, path, nodes
        #Print(current)
        if depth == 0:
            if current.is_goal(): 
                return (1, 0)
        else:
            if node_expanded >= maxnode:
                return (0, 1)
            
            branches = current.gen_choices()

            node_expanded += 1
            for direction in branches: 
                new = newstate(current, direction[1])
                (goal, end) = DFS(depth-1, new)
                
                if goal: 
                    path.append(direction[0]) 
                    #record the path by tracing back to the parents node
                    return (1, 0)
                if end: return (0, 1)

        return (0, 0)

def IDS(start, limit): #Iterative Deepening search
    global node_expanded, maxnode, path, init, nodes, maxdepth
    
    node_expanded = 0
    maxnode = limit
    path = []
    maxdepth = 0
    init = State(start)
    print("Start state:")
    init.printboard()
    print(f"{'_'*23}")
    print(f"|{'Depth':^9} | {'Expanded':^9}|")
    print(f"|{'-'*10}|{'-'*10}|")

    while (node_expanded < maxnode): #node limit
        node_expanded = 0
        nodes = []
        (goal, end) = DFS(maxdepth, init)
        if goal: 
            print(f"{'¯'*23}")
            print(f"{node_expanded} nodes expanded.")
            return list(reversed(path))
        if end: break
        print(f"|{maxdepth:>9} | {node_expanded:>9}|")
        maxdepth += 1

    print(f"{'¯'*23}")
    print(f"Limit of {maxnode} nodes Exceeded!")
    return None

def result(search_result): #result
    if search_result == None:
        print("Search not found.")
    else:
        print(f"Total {len(search_result)} moves:")
        if search_result:
            print(search_result[0], end = ' ')
            print(*['-> '+_result for _result in search_result[1:]])

def inputstate():  #input validation
    try: 
       start = list(map(int,input("Please input the start state of the puzzle\n(eg: 0 1 2 3 4 5 6 7 8): \n").split()))      
    except ValueError :
        print("Default start state (7,2,4,5,0,6,8,3,1) used!")
        return [7,2,4,5,0,6,8,3,1] 
        
    if len(start)!=9 or start.count(0)!=1:
        start = [7,2,4,5,0,6,8,3,1] 
        print("Default start state (7,2,4,5,0,6,8,3,1) used!")
    return start

def main():
    global nodes
    nodes = []
    limit = 1000000 #search limit
    result(IDS(inputstate(), limit))

main()