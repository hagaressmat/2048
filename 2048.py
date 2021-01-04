

import random

def add(matrix):
    i = random.randint(0,3)
    j = random.randint(0,3)
    while (matrix[i][j] != 0):
        i = random.randint(0,3)
        j = random.randint(0,3)
    matrix [i][j] = 2
    
def start():
    matrix = []
    matrix = [[0] * 4 for i in range(4)]
    add(matrix)
    return matrix

def state(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 2048:
                return 'WON'
    for i in range(4): 
        for j in range(4): 
            if(matrix[i][j]== 0): 
                return 'GAME NOT OVER'
    for i in range(3): 
        for j in range(3): 
            if(matrix[i][j]== mat[i + 1][j] or matrix[i][j]== matrix[i][j + 1]): 
                return 'GAME NOT OVER'
  
    for j in range(3): 
        if(matrix[3][j]== matrix[3][j + 1]): 
            return 'GAME NOT OVER'
  
    for i in range(3): 
        if(matrix[i][3]== matrix[i + 1][3]): 
            return 'GAME NOT OVER'
  
    return 'LOST'

def compress(matrix):
    is_changed = False
    new_matrix = []
    for i in range(4): 
        new_matrix.append([0] * 4)
    for i in range(4): 
        pos = 0
        
        for j in range(4): 
            if(matrix[i][j] != 0): 
                  
                new_matrix[i][pos] = matrix[i][j] 
                  
                if(j != pos): 
                    is_changed = True
                pos += 1
                
    return new_matrix, is_changed




def merge(matrix): 
      
    is_changed = False
      
    for i in range(4): 
        for j in range(3): 
  
            if(matrix[i][j] == matrix[i][j + 1] and matrix[i][j] != 0): 
   
                matrix[i][j] = matrix[i][j] * 2
                matrix[i][j + 1] = 0
  
                is_changed = True
  
    return matrix, is_changed 




def reverse(matrix): 
    new_matrix =[] 
    for i in range(4): 
        new_matrix.append([]) 
        for j in range(4): 
            new_matrix[i].append(matrix[i][3 - j]) 
    return new_matrix
  

def transpose(matrix): 
    new_matrix = [] 
    for i in range(4): 
        new_matrix.append([]) 
        for j in range(4): 
            new_matrix[i].append(matrix[j][i]) 
    return new_matrix 



def move_left(matrix): 
  
    new_matrix, is_changed1 = compress(matrix) 

    new_matrix, is_changed2 = merge(new_matrix) 
	
    is_changed = is_changed1 or is_changed2 
   
    new_matrix, temp = compress(new_matrix) 
  
    return new_matrix, is_changed 


def move_right(matrix): 
  
    new_matrix = reverse(matrix) 
  
    new_matrix, is_changed = move_left(new_matrix) 
  
    new_matrix = reverse(new_matrix) 
    return new_matrix, is_changed 


def move_up(matrix): 
  

    new_matrix = transpose(matrix) 
  

    new_matrix, is_changed = move_left(new_matrix) 
  

    new_matrix = transpose(new_matrix) 
    return new_matrix, is_changed 

def move_down(matrix): 
  
    new_matrix = transpose(matrix) 
  
    new_matrix, is_changed = move_right(new_matrix) 
    
    new_matrix = transpose(new_matrix) 
    return new_matrix, is_changed 



matrix = start() 
  
while(True): 
  
    x = input("Enter command W/S/A/D, Z to exit: ") 
  
    if(x == 'W' or x == 'w'): 
  
        matrix, flag = move_up(matrix) 
  
        status = state(matrix) 

  
        if(status == 'GAME NOT OVER'): 
            add(matrix) 
   
        else: 
            break
  
  
    elif(x == 'S' or x == 's'): 
        matrix, flag = move_down(matrix) 
        status = state(matrix) 
        if(status == 'GAME NOT OVER'): 
            add(matrix) 
        else: 
            break
        
        
    elif(x == 'A' or x == 'a'): 
        matrix, flag = move_left(matrix) 
        status = state(matrix) 
        if(status == 'GAME NOT OVER'): 
            add(matrix) 
        else: 
            break
  
    
    elif(x == 'D' or x == 'd'): 
        matrix, flag = move_right(matrix) 
        status = state(matrix) 
        if(status == 'GAME NOT OVER'): 
            add(matrix) 
        else: 
            break
    elif(x == 'z' or x == 'Z'): 
        import sys
        sys.exit()
    else: 
        print("Invalid Key Pressed") 
  
    for row in matrix:
        print (row)


