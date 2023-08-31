#!/usr/local/bin/python3
# solver2021.py : 2021 Sliding tile puzzle solver
#
# Code by: Sushant Nirantar sniranta
#
# Based on skeleton code by D. Crandall & B551 Staff, September 2021
#

import sys
from queue import PriorityQueue
ROWS=5
COLS=5

def printable_board(board):
    return [ ('%3d ')*COLS  % board[j:(j+COLS)] for j in range(0, ROWS*COLS, COLS) ]
#Function to copy list and return copy
def list_copy(lst):
    new_lst=[[0 for i in range(0,len(lst[0]))] for j in range(0,len(lst))]
    for r in range(0,len(lst)):
        for c in range(0,len(lst[0])):
            new_lst[r][c]=lst[r][c]
    return new_lst
#Check if we've reached the goal
def is_goal(state):
    tup=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
    t1=to_tuple(state)
    flag=0
    for i in range(len(tup)):
        if(tup[i]==t1[i]):
            continue
        else:
            flag=flag+1
    if(flag==0):
        return True
    else:
        return False
#Make 2-D list to tuple
def to_tuple(lst):
    lst1=[]
    for r in range(0,len(lst)):
        for c in range(0,len(lst[0])):
            lst1.append(lst[r][c])
    return tuple(lst1)
#Make tuple to a 2-D list
def make_list(initial_board):
    lst=[]
    for i in range(0,len(initial_board)):
        lst.append(initial_board[i])
    return [lst[5*i:5*(i+1)] for i in range(0,5)]
#Shifing 1st row to right
def row_1_right(lst):
    new_lst=[]
    return_lst=list_copy(lst)
    for i in range(0,len(lst[0])):
        j=(i+1)%5
        new_lst.insert(j,lst[0][i])   
    return_lst.pop(0)
    return_lst.insert(0,new_lst)
    return return_lst
#Shifting 1st row to left
def row_1_left(lst):
    new_lst=[]
    return_lst=list_copy(lst)
    for i in range(0,len(lst[0])):
        j=i-1
        if(j<0):
            j=4
        new_lst.insert(j,lst[0][i])
    return_lst.pop(0)
    return_lst.insert(0,new_lst)
    return return_lst
#Shifting 1st column down
def col_1_down(lst):
    lst1=lst
    lst1=transpose_list(lst1)
    lst1=row_1_right(lst1)
    lst1=transpose_list(lst1)
    return lst1
#Shifting 1st column up
def col_1_up(lst):
    lst1=lst
    lst1=transpose_list(lst1)
    lst1=row_1_left(lst1)
    lst1=transpose_list(lst1)
    return lst1
#Shifing 2nd row to right
def row_2_right(lst):
    new_lst=[]
    return_lst=list_copy(lst)
    for i in range(0,len(lst[0])):
        j=(i+1)%5
        new_lst.insert(j,lst[1][i])
    return_lst.pop(1)
    return_lst.insert(1,new_lst)
    return return_lst
#Shifting 2nd row to left
def row_2_left(lst):
    new_lst=[]
    return_lst=list_copy(lst)
    for i in range(0,len(lst[0])):
        j=i-1
        if(j<0):
            j=4
        new_lst.insert(j,lst[1][i])
    return_lst.pop(1)
    return_lst.insert(1,new_lst)
    return return_lst
#Shifting 2nd column down
def col_2_down(lst):
    lst1=lst
    lst1=transpose_list(lst1)
    lst1=row_2_right(lst1)
    lst1=transpose_list(lst1)
    return lst1
#Shifting 2nd column up
def col_2_up(lst):
    lst1=lst
    lst1=transpose_list(lst1)
    lst1=row_2_left(lst1)
    lst1=transpose_list(lst1)
    return lst1
#Shifing 3rd row to right
def row_3_right(lst):
    new_lst=[]
    return_lst=list_copy(lst)
    for i in range(0,len(lst[0])):
        j=(i+1)%5
        new_lst.insert(j,lst[2][i])
    return_lst.pop(2)
    return_lst.insert(2,new_lst)
    return return_lst
#Shifting 3rd row to left
def row_3_left(lst):
    new_lst=[]
    return_lst=list_copy(lst)
    for i in range(0,len(lst[0])):
        j=i-1
        if(j<0):
            j=4
        new_lst.insert(j,lst[2][i])
    return_lst.pop(2)
    return_lst.insert(2,new_lst)
    return return_lst
#Shifting 3rd column down
def col_3_down(lst):
    lst1=lst
    lst1=transpose_list(lst1)
    lst1=row_3_right(lst1)
    lst1=transpose_list(lst1)
    return lst1
#Shifting 3rd column up
def col_3_up(lst):
    lst1=lst
    lst1=transpose_list(lst1)
    lst1=row_3_left(lst1)
    lst1=transpose_list(lst1)
    return lst1
#Shifing 4th row to right
def row_4_right(lst):
    new_lst=[]
    return_lst=list_copy(lst)
    for i in range(0,len(lst[0])):
        j=(i+1)%5
        new_lst.insert(j,lst[3][i])
    return_lst.pop(3)
    return_lst.insert(3,new_lst)
    return return_lst
#Shifting 4th row to left
def row_4_left(lst):
    new_lst=[]
    return_lst=list_copy(lst)
    for i in range(0,len(lst[0])):
        j=i-1
        if(j<0):
            j=4
        new_lst.insert(j,lst[3][i])
    return_lst.pop(3)
    return_lst.insert(3,new_lst)
    return return_lst
#Shifting 4th column down
def col_4_down(lst):
    lst1=lst
    lst1=transpose_list(lst1)
    lst1=row_4_right(lst1)
    lst1=transpose_list(lst1)
    return lst1
#Shifting 4th column up
def col_4_up(lst):
    lst1=lst
    lst1=transpose_list(lst1)
    lst1=row_4_left(lst1)
    lst1=transpose_list(lst1)
    return lst1
#Shifing 5th row to right
def row_5_right(lst):
    new_lst=[]
    return_lst=list_copy(lst)
    for i in range(0,len(lst[0])):
        j=(i+1)%5
        new_lst.insert(j,lst[4][i])
    return_lst.pop(4)
    return_lst.insert(4,new_lst)
    return return_lst
#Shifting 5th row to left
def row_5_left(lst):
    new_lst=[]
    return_lst=list_copy(lst)
    for i in range(0,len(lst[0])):
        j=i-1
        if(j<0):
            j=4
        new_lst.insert(j,lst[4][i])
    return_lst.pop(4)
    return_lst.insert(4,new_lst)
    return return_lst
#Shifting 5th column down
def col_5_down(lst):
    lst1=lst
    lst1=transpose_list(lst1)
    lst1=row_5_right(lst1)
    lst1=transpose_list(lst1)
    return lst1
#Shifting 5th column up
def col_5_up(lst):
    lst1=lst
    lst1=transpose_list(lst1)
    lst1=row_5_left(lst1)
    lst1=transpose_list(lst1)
    return lst1
#Making transpose of matrix
def transpose_list(lst):
    a=[[0 for i in range(0,5)] for j in range(0,5)]
    for i in range(0,len(lst)):
        for j in range(0,len(lst)):
            a[i][j]=lst[j][i]
    return a
#row distance
def row_dist(x,a):
    if(x>=a):
        return x-a
    else:
        return a-x
#column distance
def col_dist(y,b):
    if(y>=b):
        return y-b
    else:
        return b-y
#Manhattan distance between 2 points
def dist(x,y,a,b):
    r=row_dist(x,a)
    c=col_dist(y,b)
    tot=r+c
    return tot
#Outer ring clockwise
def out_clock(lst):
    lst1=[[0 for i in range(0, len(lst))] for j in range(0,len(lst))]
    for c in range(0,len(lst[0])):
        if(c+1<len(lst[0])):
            lst1[0][c+1]=lst[0][c]
        else:
            lst1[1][len(lst)-1]=lst[0][c]
    for r in range(0,len(lst)):
        if(r+1<len(lst)):
            lst1[r+1][len(lst)-1]=lst[r][len(lst)-1]
        else:
            lst1[r][len(lst[0])-2]=lst[r][len(lst)-1]
    for c in range(len(lst[0])-1,-1,-1):
        if(c-1>=0):
            lst1[len(lst)-1][c-1]=lst[len(lst)-1][c]
        else:
            lst1[len(lst)-2][0]=lst[len(lst)-1][c]
    for r in range(len(lst)-1,-1,-1):
        if(r-1>=0):
            lst1[r-1][0]=lst[r][0]
        else:
            lst1[r][1]=lst[r][0]
    for r in range(0,len(lst)):
        for c in range(0,len(lst[0])):
            if(lst1[r][c]==0):
                lst1[r][c]=lst[r][c]
    return lst1
#Out-anti-clock
def out_anti_clock(lst):
    lst1=[[0 for i in range(0, len(lst))] for j in range(0,len(lst))]
    for c in range(len(lst[0])-1,-1,-1):
        if(c-1>=0):
            lst1[0][c-1]=lst[0][c]
        else:
            lst1[1][0]=lst[0][c]
    for r in range(0,len(lst)):
        if(r+1<len(lst)):
            lst1[r+1][0]=lst[r][0]
        else:
            lst1[r][1]=lst[r][0]
    for c in range(0,len(lst[0])):
        if(c+1<len(lst[0])):
            lst1[len(lst)-1][c+1]=lst[len(lst)-1][c]
        else:
            lst1[len(lst)-2][c]=lst[len(lst)-1][c]
    for r in range(len(lst)-1,-1,-1):
        if(r-1>=0):
            lst1[r-1][len(lst[0])-1]=lst[r][len(lst[0])-1]
        else:
            lst1[r][len(lst[0])-2]=lst[r][len(lst[0])-1]
    for r in range(0,len(lst)):
        for c in range(0,len(lst[0])):
            if(lst1[r][c]==0):
                lst1[r][c]=lst[r][c]
    return lst1
#Inner clockwise
def inner_clock(lst):
    lst1=[[0 for i in range(0, len(lst))] for j in range(0,len(lst))]
    for c in range(1,len(lst[0])-1):
        if(c+1<len(lst[0])-1):
            lst1[1][c+1]=lst[1][c]
        else:
            lst1[2][c]=lst[1][c]
    for r in range(1,len(lst)-1):
        if(r+1<len(lst)-1):
            lst1[r+1][len(lst)-2]=lst[r][len(lst)-2]
        else:
            lst1[r][len(lst[0])-3]=lst[r][len(lst)-2]
    for c in range(len(lst[0])-2,0,-1):
        if(c-1>0):
            lst1[len(lst)-2][c-1]=lst[len(lst)-2][c]
        else:
            lst1[len(lst)-3][c]=lst[len(lst)-2][c]
    for r in range(len(lst)-2,0,-1):
        if(r-1>0):
            lst1[r-1][1]=lst[r][1]
        else:
            lst1[r][2]=lst[r][1]
    for r in range(0,len(lst)):
        for c in range(0,len(lst[0])):
            if(lst1[r][c]==0):
                lst1[r][c]=lst[r][c]
    return lst1
#Inner anti clockwise
def inner_anti_clock(lst):
    lst1=[[0 for i in range(0, len(lst))] for j in range(0,len(lst))]
    for c in range(len(lst[0])-2,0,-1):
        if(c-1>0):
            lst1[1][c-1]=lst[1][c]
        else:
            lst1[2][c]=lst[1][c]
    for r in range(1,len(lst)-1):
        if(r+1<len(lst)-1):
            lst1[r+1][1]=lst[r][1]
        else:
            lst1[r][2]=lst[r][1]
    for c in range(1,len(lst[0])-1):
        if(c+1<len(lst[0])-1):
            lst1[len(lst)-2][c+1]=lst[len(lst)-2][c]
        else:
            lst1[len(lst)-3][c]=lst[len(lst)-2][c]
    for r in range(len(lst)-2,0,-1):
        if(r-1>0):
            lst1[r-1][len(lst)-2]=lst[r][len(lst)-2]
        else:
            lst1[r][len(lst)-3]=lst[r][len(lst)-2]
    for r in range(0,len(lst)):
        for c in range(0,len(lst[0])):
            if(lst1[r][c]==0):
                lst1[r][c]=lst[r][c]
    return lst1
#equal points
def equal_points(a,b,x,y):
    if(a==x and b==y):
        return True
    else:
        return False
#Defining Cyclic Manhattan distance as heuristic
def heur(lst):
    dict1={1:(0,0),2:(0,1),3:(0,2),4:(0,3),5:(0,4),6:(1,0),7:(1,1),8:(1,2),9:(1,3),10:(1,4),11:(2,0),12:(2,1),13:(2,2),14:(2,3),15:(2,4),16:(3,0),17:(3,1),18:(3,2),19:(3,3),20:(3,4),21:(4,0),22:(4,1),23:(4,2),24:(4,3),25:(4,4)}
    total=0
    for r in range(0,len(lst)):
        for c in range(0,len(lst[0])):
            total=total+min(dist(*dict1[lst[r][c]],r,c),dist(*dict1[lst[r][c]],r-5,c),dist(*dict1[lst[r][c]],r+5,c),dist(*dict1[lst[r][c]],r,c-5),dist(*dict1[lst[r][c]],r,c+5),dist(*dict1[lst[r][c]],r-5,c-5),dist(*dict1[lst[r][c]],r+5,c+5))
    return total
#Defining a second heuristic to count the number of misplaced tiles
def heur2(lst):
    dict1={1:(0,0),2:(0,1),3:(0,2),4:(0,3),5:(0,4),6:(1,0),7:(1,1),8:(1,2),9:(1,3),10:(1,4),11:(2,0),12:(2,1),13:(2,2),14:(2,3),15:(2,4),16:(3,0),17:(3,1),18:(3,2),19:(3,3),20:(3,4),21:(4,0),22:(4,1),23:(4,2),24:(4,3),25:(4,4)}
    total=0
    for r in range(0,len(lst)):
        for c in range(0,len(lst[0])):
            if(equal_points(*dict1[lst[r][c]],r,c)):
                pass
            else:
                total=total+1
    return total
#Defining Inversion, i.e. total number of tiles that are smaller than current tile
def inver(lst):
    lst_test=[]
    count=0
    for r in range(len(lst)):
        for c in range(len(lst[0])):
            lst_test.append(lst[r][c])
    for i in range(0,len(lst_test)):
        for j in range(i+1,len(lst_test)):
            if(lst_test[i]>lst_test[j]):
                count=count+1
    return count
#Defining a heuristic with both heuristic 1 and 2, dividing it by total number of tiles that can be moved for number of misplaced tiles
def heur3(lst):
    k=heur(lst)+inver(lst)
    if(heur2(lst)-inver(lst)==1 or inver(lst)-heur2(lst)==1):
        k=heur(lst)
    if(heur2(lst)<=5):
        return k/5
    elif(heur2(lst)>5 and heur2(lst)<16):
        return k/13
    else:
        return k/29
#Defining a class for node in search tree denoting the puzzle arrangement
class node:
    def __init__(self,parent,data,level,path):
        self.parent=parent
        self.data=data
        self.level=level
        self.path=path
    
    def f_function(self):
        total=self.level+heur3(self.data)
        return total
    
    def __eq__(self,other):
        return (self.f_function()==other.f_function()) and (self.get_level()==other.get_level())
    def __ne__(self,other):
        return not (self==other)
    def __lt__(self,other):
        return (self.f_function()<=other.f_function()) and (self.get_level()<other.get_level())
    def __gt__(self,other):
        return (self.f_function()>=other.f_function()) and (self.get_level()>other.get_level())
    def __le__(self,other):
        return (self<other) or (self==other)
    def __ge__(self,other):
        return (self>other) or (self==other)

    #Defining a successor function to return all possible children of a current arrangement
    def successo(self):
        lst=[]
        lst.append(node(self.data,row_1_right(self.data),self.level+1,self.path+"R1,"))
        lst.append(node(self.data,row_2_right(self.data),self.level+1,self.path+"R2,"))
        lst.append(node(self.data,row_3_right(self.data),self.level+1,self.path+"R3,"))
        lst.append(node(self.data,row_4_right(self.data),self.level+1,self.path+"R4,"))
        lst.append(node(self.data,row_5_right(self.data),self.level+1,self.path+"R5,"))
        lst.append(node(self.data,row_1_left(self.data),self.level+1,self.path+"L1,"))
        lst.append(node(self.data,row_2_left(self.data),self.level+1,self.path+"L2,"))
        lst.append(node(self.data,row_3_left(self.data),self.level+1,self.path+"L3,"))
        lst.append(node(self.data,row_4_left(self.data),self.level+1,self.path+"L4,"))
        lst.append(node(self.data,row_5_left(self.data),self.level+1,self.path+"L5,"))
        lst.append(node(self.data,col_1_up(self.data),self.level+1,self.path+"U1,"))
        lst.append(node(self.data,col_2_up(self.data),self.level+1,self.path+"U2,"))
        lst.append(node(self.data,col_3_up(self.data),self.level+1,self.path+"U3,"))
        lst.append(node(self.data,col_4_up(self.data),self.level+1,self.path+"U4,"))
        lst.append(node(self.data,col_5_up(self.data),self.level+1,self.path+"U5,"))
        lst.append(node(self.data,col_1_down(self.data),self.level+1,self.path+"D1,"))
        lst.append(node(self.data,col_2_down(self.data),self.level+1,self.path+"D2,"))
        lst.append(node(self.data,col_3_down(self.data),self.level+1,self.path+"D3,"))
        lst.append(node(self.data,col_4_down(self.data),self.level+1,self.path+"D4,"))
        lst.append(node(self.data,col_5_down(self.data),self.level+1,self.path+"D5,"))
        lst.append(node(self.data,out_clock(self.data),self.level+1,self.path+"Oc,"))
        lst.append(node(self.data,out_anti_clock(self.data),self.level+1,self.path+"Occ,"))
        lst.append(node(self.data,inner_clock(self.data),self.level+1,self.path+"Ic,"))
        lst.append(node(self.data,inner_anti_clock(self.data),self.level+1,self.path+"Icc,"))
        return lst
    #Getters for basic information of the node
    def get_data(self):
        return self.data
    def get_path(self):
        return self.path
    def get_level(self):
        return self.level
#Solve function   
def solve(initial_board):
    """
    1. This function should return the solution as instructed in assignment, consisting of a list of moves like ["R2","D2","U1"].
    2. Do not add any extra parameters to the solve() function, or it will break our grading and testing code.
       For testing we will call this function with single argument(initial_board) and it should return 
       the solution.
    3. Please do not use any global variables, as it may cause the testing code to fail.
    4. You can assume that all test cases will be solvable.
    5. The current code just returns a dummy solution.
    """
    #Make a list format of the initial board
    lst=(make_list(initial_board))
    #Set of visited nodes
    visited=set()
    #Using a priority queue as fringe
    fringe=PriorityQueue()
    #Defining the initial node with the initial board arrangement and level as 0
    N=node([],lst,0,"")
    k=N.f_function()
    fringe.put((k,N))
    while not fringe.empty():
        curr=fringe.get()[1]
        if(is_goal(curr.get_data())):
            k=curr.get_path()
            #Since I'm using string to store the path, we will split the string on ',' to get the list of moves 
            l=k.split(",")
            #The final element of the split list is " " so we need to remove it from the list
            l.pop(-1)
            #l is the optimal path to goal
            return l
            break
        else:
            if(to_tuple(curr.get_data()) in visited):
                pass
            else:
                visited.add(to_tuple(curr.get_data()))
                lst3=curr.successo()
                for i in lst3:
                   fringe.put((i.f_function(),i))


# Please don't modify anything below this line
#
if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected a board filename"))

    start_state = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            start_state += [ int(i) for i in line.split() ]

    if len(start_state) != ROWS*COLS:
        raise(Exception("Error: couldn't parse start state file"))

    print("Start state: \n" +"\n".join(printable_board(tuple(start_state))))

    print("Solving...")
    route = solve(tuple(start_state))
    print("Solution found in " + str(len(route)) + " moves:" + "\n" + " ".join(route))
