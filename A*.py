from os import system, name

class State:
    def __init__(self, l, par = None, dir = None, gn = 0):
        self.pos = l.index(0)
        self.x = self.pos%3
        self.y = self.pos//3
        self.board = l

        self.parent = par #parent of the node (default is none)
        self.dir = dir #the direction of previous move (none for the first state)
        self.gn = gn #the depth of the state in the tree

    def __eq__(self, other):
        if isinstance(other, State):
            return self.board == other.board

    def __lt__(self,other):
            return self.fn < other.fn

    def gen_choices(self): #generate possible moves
        choices = []
        if self.x>0: choices.append(('left',-1))
        if self.x<2: choices.append(('right',1))
        if self.y>0: choices.append(('up',-3))
        if self.y<2: choices.append(('down',3))
        return choices

    def h_func(self, h):
        self.fn = h + self.gn

    def is_goal(self): #goal state of lecture notes
        if self.board == goal: return 1
        else: return 0

    def printb(self):
        print(f"cost = {self.fn} with gn = {self.gn}")
        print(*[self.board[i] if i%3!=0 or i==0 else '\n'+str(self.board[i]) for i in range(len(self.board))])
        print()
    
def newstate(parent, dir, indx): #generate a new state for the child node 
    newboard = parent.board.copy()
    p = parent.pos
    newboard[p],newboard[p+indx] = newboard[p+indx], newboard[p]
    return State(newboard, parent, dir, parent.gn+1)

def xycal(pos): #return the xy coordinates
    return pos%3,pos//3

def manhattan_dis(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def h1(current): # Heuristic function 1: number of misplaced tiles
    count = 0
    for tile in range(1,9):
        if current.board.index(tile) != goal.index(tile): count += 1
    return count

def h2(current): # Heuristic function 2: total manhattan distance
    count = 0
    for tile in range(1,9):
        count += manhattan_dis(*xycal(current.board.index(tile)),*xycal(goal.index(tile)))
    return count

def clear(): #clear screen
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

def printl(l): #print the board
    print(*[l[i] if i%3!=0 or i==0 else '\n'+str(l[i]) for i in range(len(l))])

def Print(current): #animation
    clear()
    print("Start state:")
    printl(start)
    print(f'Nodes expanded = {node_expanded}')
    current.printb()

def search(current):  # A* search using heuristic 1
    global node_expanded, nodes_reached, goal, costs_list

    while (True):
        current = costs_list[0]

        Print(current)

        if current not in nodes_reached:
            
            nodes_reached.append(current)
    
            if current.is_goal(): break

            costs_list.remove(current) #expand the least cost node
            for choice in current.gen_choices():
                child = newstate(current, *choice)
                child.h_func(h1(child))

                if child not in costs_list:
                    costs_list.append(child)

            node_expanded += 1
            costs_list = sorted(costs_list)
            # sort the costs_list so that the first element in the list most have the least cost

        else: costs_list.pop(0)

    return current

def search2(current):  # A* search using heuristic 2
    global node_expanded, nodes_reached, goal, costs_list

    while (True):
        current = costs_list[0]

        Print(current)

        if current not in nodes_reached:
            nodes_reached.append(current)
    
            if current.is_goal(): break

            costs_list.remove(current)
            for choice in current.gen_choices():
                child = newstate(current, *choice)
                child.h_func(h2(child))

                if child not in costs_list:
                    costs_list.append(child)
                    
            node_expanded += 1
            costs_list = sorted(costs_list)

        else: costs_list.pop(0)

    return current

#A* search algorithm
def AS(start):
    global goal, node_expanded, nodes_reached, costs_list

    node_expanded = 0
    goal = [0,1,2,3,4,5,6,7,8]
    nodes_reached = []
    costs_list = []
    
    init = State(start)
    costs_list.append(init)

    h = int(input("h1 or h2: "))  #ask the user to choose the heuristics for searching
    if h==1:
        init.h_func(h1(init))
        found = search(init)
    else: 
        init.h_func(h2(init))
        found = search2(init)
    
    path = []
    print(f"Total {node_expanded} nodes expanded.")
    #trace back to the parent state to get the directions 
    while found.parent!=None:
        path.append(found.dir)
        found = found.parent

    del node_expanded, nodes_reached, costs_list
    return list(reversed(path))


def result(search_result): #result
    if search_result == None:
        print("Search not found.")
    else:
        print(f"Total {len(search_result)} moves:")
        print(search_result[0], end = ' ')
        print(*['-> '+_result for _result in search_result[1:]])

def inputstate():  #input validation
    try: 
       start = list(map(int,input("Please input the start state of the puzzle\n(eg: 0 1 2 3 4 5 6 7 8): \n").split()))      
    except ValueError :
        print("Default start state (7,2,4,5,0,6,8,3,1) used!")
        return [7,2,4,5,0,6,8,3,1] #start state from fig 3.25, p.25 of lecture notes of chp4
        
    if len(start)!=8 or start.count(0)!=1:
        start = [7,2,4,5,0,6,8,3,1] 
        print("Default start state (7,2,4,5,0,6,8,3,1) used!")
    return start

def main():
    global start
    clear()
    start = inputstate()
    result(AS(start))

main()