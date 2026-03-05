import random
from collections import deque

grid = [['','',''],['','',''],['','','']]

def grid_to_string(grid):
    return ''.join(cell if cell != '' else '_' for row in grid for cell in row)

def string_to_grid(state):
    return [[state[3*i + j] if state[3*i + j] != '_' else '' for j in range(3)] for i in range(3)]

def print_grid():
    for row in grid:
        print(f'{row}\n')

def backtracking(G,parent):
    path = []
    while G is not None:
        path.append(G)
        G = parent[G]
    return path[-2]

def count_x(grid):
    count = 0
    for row in range(3):
        for i in range(3):
            if grid[row][i] == 'x':
                  count += 1
    return count

def count_o(grid):
    count = 0
    for row in range(3):
        for i in range(3):
            if grid[row][i] == 'o':
                  count += 1
    return count

def BFS(grid):
    current = grid_to_string(grid)
    parent = {}
    queue = deque()
    parent[current] = None
    queue.append(current)
    visited_states = set()
    visited_states.add(current)

    while queue:
        current = queue.popleft()
        current_grid = string_to_grid(current)
        if (
            (current_grid[0][0] == current_grid[0][1] == current_grid[0][2] == 'x') or
            (current_grid[1][0] == current_grid[1][1] == current_grid[1][2] == 'x') or
            (current_grid[2][0] == current_grid[2][1] == current_grid[2][2] == 'x') or
            (current_grid[0][0] == current_grid[1][0] == current_grid[2][0] == 'x') or
            (current_grid[0][1] == current_grid[1][1] == current_grid[2][1] == 'x') or
            (current_grid[0][2] == current_grid[1][2] == current_grid[2][2] == 'x') or
            (current_grid[0][0] == current_grid[1][1] == current_grid[2][2] == 'x') or
            (current_grid[0][2] == current_grid[1][1] == current_grid[2][0] == 'x') ): 
                 continue
        board_is_full = True
        for row in range(3):
              for col in range(3):
                    if current_grid[row][col] == '':
                          board_is_full = False
                          break
        if board_is_full == True:
              continue
        
        for row in range(3):
            for col in range(3):
                if current_grid[row][col] == '':
                    new_grid = [r[:] for r in current_grid]
                    count_of_x = count_x(current_grid)
                    count_of_o = count_o(current_grid)
                    if count_of_x > count_of_o:
                          new_grid[row][col] = 'o'
                    elif count_of_x == count_of_o:
                          new_grid[row][col] = 'x'
                    child = grid_to_string(new_grid)

                    if child not in visited_states:
                        visited_states.add(child)
                        parent[child] = current
                        queue.append(child)

                        if (
                            (new_grid[0][0] == new_grid[0][1] == new_grid[0][2] == 'o') or
                            (new_grid[1][0] == new_grid[1][1] == new_grid[1][2] == 'o') or
                            (new_grid[2][0] == new_grid[2][1] == new_grid[2][2] == 'o') or
                            (new_grid[0][0] == new_grid[1][0] == new_grid[2][0] == 'o') or
                            (new_grid[0][1] == new_grid[1][1] == new_grid[2][1] == 'o') or
                            (new_grid[0][2] == new_grid[1][2] == new_grid[2][2] == 'o') or
                            (new_grid[0][0] == new_grid[1][1] == new_grid[2][2] == 'o') or
                            (new_grid[0][2] == new_grid[1][1] == new_grid[2][0] == 'o')
                        ):
                            optimal_state = backtracking(child,parent)
                            optimal_grid = string_to_grid(optimal_state)
                            for i in range(3):
                                for j in range(3):
                                    grid[i][j] = optimal_grid[i][j]
                            return
                        
                        flag = True
                        for row in range(3):
                            for col in range(3):
                                if current_grid[row][column] == '':
                                    flag = False
                                    break

                        if flag == True:
                              optimal_state = backtracking(child,parent)
                              optimal_grid = string_to_grid(optimal_state)
                              for i in range(3):
                                for j in range(3):
                                    grid[i][j] = optimal_grid[i][j]
                              return 
                        
game_on = True
while game_on:
      row = int(input('Which row?'))
      column = int(input('Which column?'))
      grid[row][column] = 'x'
      print_grid()
      if (grid[0][0] == grid[0][1] == grid[0][2] == 'x') or (grid[1][0] == grid[1][1] == grid[1][2] == 'x') or (grid[2][0] == grid[2][1] == grid[2][2] == 'x'):
                    print("Winner is Human")
                    break
      elif (grid[0][0] == grid[1][0] == grid[2][0] == 'x') or (grid[0][1] == grid[1][1] == grid[2][1] == 'x') or (grid[0][2] == grid[1][2] == grid[2][2] == 'x'):
                    print("Winner is Human")
                    break
      elif (grid[0][0] == grid[1][1] == grid[2][2] == 'x') or (grid[0][2] == grid[1][1] == grid[2][0] == 'x'):
                    print("Winner is Human")
                    break
      
      BFS(grid)
      print_grid()
      if (grid[0][0] == grid[0][1] == grid[0][2] == 'o') or (grid[1][0] == grid[1][1] == grid[1][2] == 'o') or (grid[2][0] == grid[2][1] == grid[2][2] == 'o'):
                    game_on = False
                    print("Winner is AI")
      elif (grid[0][0] == grid[1][0] == grid[2][0] == 'o') or (grid[0][1] == grid[1][1] == grid[2][1] == 'o') or (grid[0][2] == grid[1][2] == grid[2][2] == 'o'):
                    game_on = False
                    print("Winner is AI")
      elif (grid[0][0] == grid[1][1] == grid[2][2] == 'o') or (grid[0][2] == grid[1][1] == grid[2][0] == 'o'):
                    game_on = False
                    print("Winner is AI") 
      

