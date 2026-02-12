def checkmate(board):
  check_k = False
  grid = board.strip().split("\n")
  print(grid)
  size = len(grid[0])
  print(size)

  print(grid.count("K"))

  if board.count("K") >= 2:
    print("Not Only One King")
    return

  target = ""

  try:
    for row in range(size):
      if check_k == True:
        break
      target = ""
      for col in range(size):
        target = ""
        if grid[row][col] in ("P", "B", "R", "Q"):
          target = grid[row][col]
          print(target)
          x, y = row, col
          print(row, col)
        
        if target == "P":
          target == ""
          check_k = pawn(x, y, grid, size, check_k)
        elif target == "B":
          target == ""
          check_k = bishop(x, y, grid, size, check_k)
        elif target == "R":
          target == ""
          check_k = rook(x, y, grid, size, check_k)
        elif target == "Q":
          target == ""
          check_k = queen(x, y, grid, size, check_k)
  except:
    print("Error Triggered")

      

  print(size)
  print(grid)
  print()
  print("Result: ", end="")

  if check_k == True:
      print("Success")
  else:
      print("Fail")



def pawn(x, y, grid, size, check_k):
  if x == 0:
    pass
  elif y == 0:
    print("most left")
    print(x - 1, y + 1)
    print(grid[x - 1][y + 1])
    if grid[x - 1][y + 1] == "K":
      check_k = True
      return check_k
  elif y == size -1:
    print("most right")
    print(x - 1, y - 1)
    print(grid[x - 1][y - 1])
    if grid[x - 1][y - 1] == "K":
      check_k = True
      return check_k
  else:
    print("left right check")
    print("left")
    print(x - 1, y - 1)
    print(grid[x - 1][y - 1])
    print("-----")
    print("right")
    print(x - 1, y + 1)
    print(grid[x - 1][y + 1])
    print("-----")
    if grid[x - 1][y - 1] == "K" or grid[x - 1][y + 1] == "K":
      check_k = True
      print(check_k)
      return check_k


def rook(x, y, grid, size, check_k):
  print("rook")
  #up
  print("up")
  for i in range(x-1, -1, -1):
    if x == 0:
      break
    elif grid[i][y] in ("P", "B", "R", "Q"):
      if x != i:
        break
    elif grid[i][y] == "K":
      check_k = True
      print(check_k)
      return check_k
    print(grid[i][y])
  #down
  print("down")
  for i in range(x+1, size):
    if x == size -1:
      break
    elif grid[i][y] in ("P", "B", "R", "Q"):
      if x != i:
        break
    elif grid[i][y] == "K":
      check_k = True
      print(check_k)
      return check_k
    print(grid[i][y])
  #left
  print("left")
  for i in range(y-1, -1, -1):
    if y == 0:
      break
    elif grid[x][i] in ("P", "B", "R", "Q"):
      break
    elif grid[x][i] == "K":
      check_k = True
      print(check_k)
      return check_k
    print(grid[x][i])
  #right
  print("right")
  for i in range(y+1, size):
    if y == size -1:
      print("lnw")
      break
    elif grid[x][i] in ("P", "B", "R", "Q"):
      break
    elif grid[x][i] == "K":
      check_k = True
      print(check_k)
      return check_k
    print(grid[x][i])

  print("-------------")

def bishop(x, y, grid, size, check_k):

  print("-------------")
  print("Bishop")
  print(x, y)
  print(grid[x][y])

  #up right
  tx, ty = x, y
  print("up right")
  for _ in range(size):
    if tx <= 0 or ty >= size -1:
      break
    tx -= 1
    ty += 1
    print(tx, ty)
    print(grid[tx][ty])
    if grid[tx][ty] in ("P", "B", "R", "Q"):
      break
    elif grid[tx][ty] == "K":
      check_k = True
      print(check_k)
      return check_k
  print("-----")

  #up left
  tx, ty = x, y
  print("up left")
  for _ in range(size):
    if tx <= 0 or ty <= 0:
      break
    tx -= 1
    ty -= 1
    print(tx, ty)
    print(grid[tx][ty])
    if grid[tx][ty] in ("P", "B", "R", "Q"):
      break
    elif grid[tx][ty] == "K":
      check_k = True
      print(check_k)
      return check_k
  print("-----")
  

  print("-------------")

  #down right
  tx, ty = x, y
  print("down right")
  for _ in range(size):
    if tx >= size -1 or ty >= size -1:
      break
    tx += 1
    ty += 1
    print(tx, ty)
    print(grid[tx][ty])
    if grid[tx][ty] in ("P", "B", "R", "Q"):
      break
    elif grid[tx][ty] == "K":
      check_k = True
      print(check_k)
      return check_k
  print("-----")

  #down left
  tx, ty = x, y
  print("down left")
  for _ in range(size):
    print(tx, ty)
    if tx >= size -1 or ty <= 0:
      break
    tx += 1
    ty -= 1
    print(tx, ty)
    print(grid[tx][ty])
    if grid[tx][ty] in ("P", "B", "R", "Q"):
      break
    elif grid[tx][ty] == "K":
      check_k = True
      print(check_k)
      return check_k
  print("-----")

def queen(x, y, grid, size, check_k):
  check = rook(x, y, grid, size, check_k)
  if check == True:
    return check
  check = bishop(x, y, grid, size, check_k)
  if check == True:
    return check
