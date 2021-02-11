# Pirple Python Assignment 6 - loops #2
# draw a tick tack toe board with the passed dimentions 

def drawBoard(rows, columns):
  if columns % 2 == 0: #the board does not look right unles there is an odd number of columns
    columns += columns
  if rows < 3 or columns < 3 : #set minimum board size
    return False
  if rows > 51 or columns > 51 : #set max board size
    return False
  for i in range(rows):
    for j in range(columns):
      if i % 2 == 1:
        print("-" * columns)
        break
      else:
        if j == columns-1 and (columns-1) % 2 == 0 :
          print(" ")
        elif j == columns-1 and (columns-1) % 2 == 1 :
          print("|")
        elif j % 2 == 0:
          print(" ", end="")
        else:
          print("|", end="")
  return True


drawBoard(5,5) #traditional tick tack toe board size
drawBoard(50,50) #large board