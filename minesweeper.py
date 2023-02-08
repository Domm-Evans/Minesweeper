# #task 23
# #compulsory task 1



def minesweeper_function(minesweeper):
    #loop through every element of each list and change to int 0 if not a mine
    for i, row in enumerate(minesweeper):
        for j, col in enumerate(row):
            if col != "#":
                minesweeper[i][j] = 0

    #loop through each row of the 2d list
    for i, row in enumerate(minesweeper):
        #loop through each column of the inner list
        for j, col in enumerate(row):
            try:
                #if a mine is found at the index check all surrounding indexes for mines and add 1 to counter for every mine              
                if minesweeper[i][j]!= "#":
                    #keep the indexes within the bounds of the grid
                    if minesweeper[i-1][j-1] == "#"and 0 <= i-1 <= len(minesweeper) and 0 <= j-1 <= len(minesweeper):
                        minesweeper[i][j] += 1
                    if minesweeper[i-1][j] == "#" and 0 <= i-1 <= len(minesweeper) and 0 <= j <= len(minesweeper):
                        minesweeper[i][j] += 1
                    if minesweeper[i-1][j+1] == "#" and 0 <= i-1 <= len(minesweeper) and 0 <= j+1 <= len(minesweeper):
                        minesweeper[i][j] += 1
                    if minesweeper[i][j-1] == "#" and 0 <= i <= len(minesweeper) and 0 <= j-1 <= len(minesweeper):
                        minesweeper[i][j] += 1        
                    if minesweeper[i][j+1] == "#" and 0 <= i <= len(minesweeper) and 0 <= j+1 <= len(minesweeper):
                        minesweeper[i][j] += 1     
                    if minesweeper[i+1][j-1] == "#" and 0 <= i+1 <= len(minesweeper) and 0 <= j-1 <= len(minesweeper):
                        minesweeper[i][j] += 1     
                    if minesweeper[i+1][j] == "#" and 0 <= i+1 <= len(minesweeper) and 0 <= j <= len(minesweeper):
                        minesweeper[i][j] += 1     
                    if minesweeper[i+1][j+1] == "#" and 0 <= i+1 <= len(minesweeper) and 0 <= j+1 <= len(minesweeper):
                        minesweeper[i][j] += 1     
            #for error indexerror when indexing outside of the grid continue
            except IndexError:
                continue
    print(f"{minesweeper[0]}\n{minesweeper[1]}\n{minesweeper[2]}\n{minesweeper[3]}\n{minesweeper[4]}")

grid = [ ["-", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "-", "-"] ]

minesweeper_function(grid)