import random
grid = [['','',''],['','',''],['','','']]
parent = {}
visited_states = set()

def grid_to_string(grid):
    return ''.join(cell if cell != '' else '_' for row in grid for cell in row)

def string_to_grid(state):
    return [[state[3*i + j] if state[3*i + j] != '_' else '' for j in range(3)] for i in range(3)]

def print_grid():
    for row in grid:
        print(f'{row}\n')

def count_x(grid):
    count = 0
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'x':
                  count += 1
    return count

def count_o(grid):
    count = 0
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'o':
                  count += 1
    return count

def reset():
      global visited_states
      visited_states = set()

def DBDFS(grid,depth):
       current = grid_to_string(grid)
       if current not in visited_states:
             visited_states.add(current)
            
       current_grid = string_to_grid(current)

       if (
            (current_grid[0][0] == current_grid[0][1] == current_grid[0][2] == 'o') or
            (current_grid[1][0] == current_grid[1][1] == current_grid[1][2] == 'o') or
            (current_grid[2][0] == current_grid[2][1] == current_grid[2][2] == 'o') or
            (current_grid[0][0] == current_grid[1][0] == current_grid[2][0] == 'o') or
            (current_grid[0][1] == current_grid[1][1] == current_grid[2][1] == 'o') or
            (current_grid[0][2] == current_grid[1][2] == current_grid[2][2] == 'o') or
            (current_grid[0][0] == current_grid[1][1] == current_grid[2][2] == 'o') or
            (current_grid[0][2] == current_grid[1][1] == current_grid[2][0] == 'o')):
                return True

       if (
        (current_grid[0][0] == current_grid[0][1] == current_grid[0][2] == 'x') or
        (current_grid[1][0] == current_grid[1][1] == current_grid[1][2] == 'x') or
        (current_grid[2][0] == current_grid[2][1] == current_grid[2][2] == 'x') or
        (current_grid[0][0] == current_grid[1][0] == current_grid[2][0] == 'x') or
        (current_grid[0][1] == current_grid[1][1] == current_grid[2][1] == 'x') or
        (current_grid[0][2] == current_grid[1][2] == current_grid[2][2] == 'x') or
        (current_grid[0][0] == current_grid[1][1] == current_grid[2][2] == 'x') or
        (current_grid[0][2] == current_grid[1][1] == current_grid[2][0] == 'x') ): 
              return False
       
       board_is_full = True
       for row in range(3):
            for col in range(3):
                if current_grid[row][col] == '':
                    board_is_full = False
                    break
       if board_is_full == True:
            return False
       
       if depth == 0:
             return False

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
                          if DBDFS(new_grid,depth - 1):
                                return new_grid
       return False
       
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
      
      reset()
      depth = 4
      final_grid = DBDFS(grid,depth)
      if final_grid == False:
             final_grid = DBDFS(grid,depth + 1)
             if final_grid == False:
                    print("No optimal solution found")
                    game_on = False
                    continue
      grid = final_grid
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
      
