from tkinter import *

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)  #i - row  j - col
    return None


def solve_board(board):
    if isValidSudoku(board):
        temp = find_empty(board)
        if not temp:
            return True
        else:
            row,col = temp

        for i in range(1,10):
            if isValid(board, i, (row,col)):
                board[row][col] = i

                if solve_board(board):
                    return True
                
                board[row][col] = 0
        return board
    else:
        return False


def isValid(board,value,position):
    for i in range(len(board[0])):
        if board[position[0]][i] == value and i != position[1]:
            return False
        
        if board[i][position[1]] == value and i != position[0]:
            return False
        
        row_box = position[1]//3
        col_box = position[0]//3

        for i in range(col_box*3,col_box*3 + 3):
            for j in range(row_box*3,row_box*3 + 3):
                if board[i][j] == value and (i,j) != position:
                    return False
        return True



def isValidSudoku(board):
    for i in range(9):
        # create empty dictionaries to keep track of row, column, and block values
        row = {}
        column = {}
        block = {}
        # calculate the starting index of the current 3x3 block
        row_cube = 3 * (i//3)
        column_cube = 3 * (i%3)
        for j in range(9):
            # check if the value in the current cell of the row is valid
            if board[i][j]!=0 and board[i][j] in row:
                return False
            row[board[i][j]] = 1  # add the value to the row dictionary
            
            # check if the value in the current cell of the column is valid
            if board[j][i]!=0 and board[j][i] in column:
                return False
            column[board[j][i]] = 1  # add the value to the column dictionary
            
            # calculate the row and column index of the current cell within the 3x3 block
            rc = row_cube+j//3
            cc = column_cube + j%3
            
            # check if the value in the current cell of the block is valid
            if board[rc][cc] in block and board[rc][cc]!=0:
                return False
            block[board[rc][cc]] = 1  # add the value to the block dictionary
    return True



root = Tk()
root.title('Soduku Solver')
root.geometry('526x743')
root.configure(bg = '#91abc6')
root.resizable(False,False)

label = Label(root, text='Soduku Solver', font=('fortune',54), bg='#91abc6')
label.place(x=0, y=10, width=526)

label = Label(root, text = '', fg = '#1e54a4', bg = '#91abc6', font=('TkDefualtFont',14))
label.place(x=0, y=92, width=526)

cells = {}

def ValidateNumber(P):
    out = (P.isdigit() or P == '') and len(P) < 2
    return out

reg = root.register(ValidateNumber)

def drawGrid():
    frame = Frame(root, bg='#91abc6')
    frame.place(x=42, y=151, width=443)
    font = ('TkTextFont', 14)


    for i in range(9):
        for j in range(9):
            entry = Entry(frame,bg='#ffffff', fg='#000000', font = font, borderwidth=5, highlightbackground='#000000', relief=FLAT, justify='center', validate = 'key', validatecommand=(reg,'%P'))

            entry.place(x=i*49, y=j*49, width=48, height=48)
            cells[(i+2,j+1)] = entry

    for i in range(-1,9,3):
        Frame(frame, bg = '#000000', width=441).place(x=0, y=(i+1)*49, height=2)
    
    for j in range(-1,9,3):
        Frame(frame, bg = '#000000', width=2).place(x=(j+1)*49, y=0, height=441)



def clearValues():
    label.configure(text='')
    for row in range(2,11):
        for col in range(1,10):
            cell = cells[(row,col)]
            cell.delete(0, 'end')


def getValues():
    board = []
    label.configure(text='')
    for row in range(2,11):
        rows = []
        for col in range(1,10):
            val = cells[(row,col)].get()
            if val == '':
                rows.append(0)
            else:
                rows.append(int(val))

        board.append(rows)
    updateValues(board)

btn = Button(root, command=getValues, text='Solve',width=10, font=('TkTextFont',14))
btn.place(x=25, y=650)

btn = Button(root, command=clearValues, text='Clear', width=10, font=('TkTextFont',14))
btn.place(x=198, y=650)

btn = Button(root, command=root.destroy, text='Exit', width=10, font=('TkTextFont',14))
btn.place(x=370, y=650)


drawGrid()



def updateValues(s):
    sol = solve_board(s)
    if sol:
        for rows in range(2,11):
            for col in range(1,10):
                cells[(rows,col)].delete(0,'end')
                cells[(rows,col)].insert(0,sol[rows-2][col-1])
        label.configure(text='Soduku Solved')
    else:
        label.configure(text='Solution does not exist for this Soduku')


root.mainloop()












































