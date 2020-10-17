from tkinter import *
import random
import copy
root = Tk()

class Sudoku():

    def __init__(self, root):
        self.xIndx = None
        self.yIndx = None
        self.Window(root)
        self.drawButton(root)
        self.y_size = 68.8
        self.x_size = 151.11
        self.selected = None
        self.rect = False
        self.already = None
        self.done = False
        self.root = root
        self.res = False
        self.grid = [[0,0,3,4,0,0,3,5,0],
                     [0,0,3,4,0,0,3,5,0],
                     [0,0,3,4,0,0,3,5,0],
                     [0,0,3,4,0,0,3,5,0],
                     [0,0,3,4,0,0,3,5,0],
                     [0,0,3,4,0,0,3,5,0],
                     [0,0,3,4,0,0,3,5,0],
                     [0,0,3,4,0,0,3,5,0],
                     [0,0,3,4,0,0,3,5,0]]
        self.board = [[0 for i in range(9)] for i in range(9)]
        self.choose_level()
        self.solve()
        self.key_pressed = None
    
    def solve(self):
        lst = list(range(1,10))
        random.shuffle(lst)
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find
        for i in lst:
            if self.valid(i, find):
                self.board[row][col] = i

                if self.solve():
                    return True

                self.board[row][col] = 0 
        return False
    
    def valid(self, num, pos):
        for i in range(9):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False
        for i in range(9):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_y*3, box_y*  3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if self.board[i][j] == num and (i, j) != pos:
                    return False
        return True

    def choose_level(self):
        self.easy = Button(self.root, text='easy', command = self.easy_level)
        self.easy.place(x=60, y = 10, height = 20, width = 35)

        self.medium = Button(self.root, text='medium', command = self.medium_level)
        self.medium.place(x=100, y = 10, height = 20, width = 55)

        self.hard = Button(self.root, text='hard', command = self.hard_level)
        self.hard.place(x=160, y = 10, height = 20, width = 35)
    
    def easy_level(self, count=0):
        lst = list(range(9))
        if count == 1: #25
            self.medium["state"] = "disabled"
            self.easy["state"] = "disabled"
            self.hard["state"] = "disabled"
            self.board_2 = copy.deepcopy(self.board)
            self.draw_grid()
            return
        for i in range(9):
            random.shuffle(lst)
            self.board[i][lst[0]] = ''
            count += 1 
            if count == 1: #25
                self.medium["state"] = "disabled"
                self.easy["state"] = "disabled"
                self.hard["state"] = "disabled"
                self.board_2 = copy.deepcopy(self.board)
                self.draw_grid()
                return
        else:
            self.easy_level(count)
    
    def hard_level(self, count = 0):
        lst = list(range(9))
        if count == 60:
            self.medium["state"] = "disabled"
            self.easy["state"] = "disabled"
            self.hard["state"] = "disabled"
            self.board_2 = copy.deepcopy(self.board)
            self.draw_grid()
            return
        for i in range(9):
            random.shuffle(lst)
            self.board[i][lst[0]] = ''
            count += 1
            if count == 60:
                self.medium["state"] = "disabled"
                self.easy["state"] = "disabled"
                self.hard["state"] = "disabled"
                self.board_2 = copy.deepcopy(self.board)
                self.draw_grid()
                return
        else:
            self.hard_level(count)
    
    def medium_level(self, count = 0):
        print('medium')
        lst = list(range(9))
        if count == 40:
            self.medium["state"] = "disabled"
            self.easy["state"] = "disabled"
            self.hard["state"] = "disabled"
            self.board_2 = copy.deepcopy(self.board)
            self.draw_grid()
            return
        for i in range(9):
            random.shuffle(lst)
            self.board[i][lst[0]] = ''
            count += 1
            if count == 40:
                self.medium["state"] = "disabled"
                self.easy["state"] = "disabled"
                self.hard["state"] = "disabled"
                self.board_2 = copy.deepcopy(self.board)
                self.draw_grid()
                return
        else:
            self.medium_level(count)
    
    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0 or self.board[i][j] == '':
                    return (i, j)
        return None 
    def reset(self):
        self.delete_text()
        self.Window(self.root)
        self.drawButton(self.root)
        self.board = [[0 for i in range(9)] for i in range(9)]
        self.choose_level()
        self.solve()
    def get_indx(self, x, y):
        if y > 40 and y < 108.8:
            self.yIndx = 0
            self.selected = True
        if y > 108.8 and y < 176.8:
            self.yIndx = 1
            self.selected = True
        if y > 176.6 and y < 245.4:
            self.yIndx = 2
            self.selected = True
        if y > 245.4 and y < 314.2:
            self.yIndx = 3
            self.selected = True
        if y > 314.2 and y < 383:
            self.yIndx = 4
            self.selected = True
        if y > 383 and y < 451.8:
            self.yIndx = 5
            self.selected = True
        if y > 451.8 and y < 520.6:
            self.yIndx = 6
            self.selected = True
        if y > 520.6 and y < 589.4:
            self.yIndx = 7
            self.selected = True
        if y > 589.4 and y < 659.2:
            self.yIndx = 8
            self.selected = True
        if x > 20.1 and x < 171.21:
            self.xIndx = 0
            self.selected = True
        if x > 171.21 and x < 322.32:
            self.xIndx = 1
            self.selected = True
        if x > 322.32 and x < 473.43:
            self.xIndx = 2
            self.selected = True
        if x > 473.43 and x < 624.54:
            self.xIndx = 3
            self.selected = True
        if x > 624.54 and x < 775.65:
            self.xIndx = 4
            self.selected = True
        if x > 775.65 and x < 926.76:
            self.xIndx = 5
            self.selected = True
        if x > 926.76 and x < 1077.87:
            self.xIndx = 6
            self.selected = True
        if x > 1077.87 and x < 1228.98:
            self.xIndx = 7
            self.selected = True
        if x > 1228.98 and x < 1380:
            self.xIndx = 8
            self.selected = True
        return (self.xIndx, self.yIndx)
    def motion(self, event):
        x, y = event.x, event.y
        self.x = x
        self.y = y
        if x == None and y == None:
            pass
        elif self.x > 20.1 and self.x < 1379.9 and self.y > 40 and self.y < 660:
            if y > 40 and y < 108.8:
                self.yIndx = 0
                self.selected = True
            if y > 108.8 and y < 176.8:
                self.yIndx = 1
                self.selected = True
            if y > 176.6 and y < 245.4:
                self.yIndx = 2
                self.selected = True
            if y > 245.4 and y < 314.2:
                self.yIndx = 3
                self.selected = True
            if y > 314.2 and y < 383:
                self.yIndx = 4
                self.selected = True
            if y > 383 and y < 451.8:
                self.yIndx = 5
                self.selected = True
            if y > 451.8 and y < 520.6:
                self.yIndx = 6
                self.selected = True
            if y > 520.6 and y < 589.4:
                self.yIndx = 7
                self.selected = True
            if y > 589.4 and y < 659.2:
                self.yIndx = 8
                self.selected = True
            if x > 20.1 and x < 171.21:
                self.xIndx = 0
                self.selected = True
            if x > 171.21 and x < 322.32:
                self.xIndx = 1
                self.selected = True
            if x > 322.32 and x < 473.43:
                self.xIndx = 2
                self.selected = True
            if x > 473.43 and x < 624.54:
                self.xIndx = 3
                self.selected = True
            if x > 624.54 and x < 775.65:
                self.xIndx = 4
                self.selected = True
            if x > 775.65 and x < 926.76:
                self.xIndx = 5
                self.selected = True
            if x > 926.76 and x < 1077.87:
                self.xIndx = 6
                self.selected = True
            if x > 1077.87 and x < 1228.98:
                self.xIndx = 7
                self.selected = True
            if x > 1228.98 and x < 1380:
                self.xIndx = 8
                self.selected = True
        else:
            pass
        if self.selected == True:
            if self.rect:
                self.canvas.delete(self.rect)
            self.currentX = self.xIndx
            self.currentY = self.yIndx
            self.rect = self.canvas.create_rectangle(20 + (self.xIndx * self.x_size), 40 + self.yIndx * self.y_size, 20 + (self.xIndx * self.x_size) + self.x_size,40 + (self.yIndx * self.y_size) + self.y_size, outline="#fb0")

    def key(self, event):
        #self.already = self.board[self.yIndx][self.xIndx]
        lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.key_pressed = event.char
        self.res = isinstance(self.board_2[self.currentY][self.currentX], str) 
        if self.key_pressed in lst and self.rect and self.res == True: 
            self.canvas.delete('delete')
            self.board[self.currentY][self.currentX] = int(event.char)
            self.board_2[self.currentY][self.currentX] = event.char
            self.draw_grid()
            # arrY = {0: 74.4, 1: 143.28, 2: 212.6, 3: 281.04, 4: 349.92, 5: 418.8, 6: 487.68, 7: 556.56, 8: 625.44}
            # arrX = {0: 95.55, 1: 246.66, 2: 397.77, 3: 548.88, 4: 699.99, 5: 851.1, 6: 1002.21, 7: 1153.32, 8: 1304.43}
            # y =  arrY[self.yIndx]
            # x = arrX[self.xIndx]
            #self.text_place(x, y, int(event.char))
        find = self.find_empty()
        if not find:
            done = True
            for i in range(9):
                for j in range(9):
                    if self.valid(self.board[i][j], (i, j)):
                        pass
                    else:
                        done = False
            if done:
                self.canvas.delete("all")
                self.canvas.create_text(684, 300, font=("Purisa", 170), text = 'You Win', width = 5000)
                
    
    def Window(self, main):
        main.title("Sudoku")
        root.geometry("1400x700")
        
        # Gets both half the screen width/height and window width/height
        positionRight = int(root.winfo_screenwidth()/2 - 1400/2)
        positionDown = int(root.winfo_screenheight()/2 - 700/2)
        
        # Positions the window in the center of the page.
        root.geometry("+{}+{}".format(positionRight, positionDown))
        
        self.canvas = Canvas(main)
        self.canvas.create_rectangle(20, 40, 1380, 660, outline="#fb0")
        self.canvas.pack(fill=BOTH, expand=1)
        cell_size = 108.8
        for i in range(1, 9):
            if i % 3 == 0:
                self.canvas.create_line(20, cell_size, 1380, cell_size, width=2.5)
                cell_size += 68.8
            else:
                self.canvas.create_line(20, cell_size, 1380, cell_size, width=1.35)
                cell_size += 68.8
        cell_width = 171.11
        for j in range(1, 9):
            if j % 3 == 0:
                self.canvas.create_line(cell_width, 40, cell_width, 660, width=2.5)
                cell_width += 151.11
            else:
                self.canvas.create_line(cell_width, 40, cell_width, 660, width=1.35)
                cell_width += 151.11  
    
    def start_game(self):
        start = [[0 for i in range(9)] for j in range(9)]
        for k in [0, 3, 6] :
            fill = list(range(1, 10, 1))
            for i in range(k, k + 3) :
                for j in range(k, k + 3) :
                    num = fill[random.randrange(0, len(fill), 1)]
                    start[i][j] = num
                    fill.remove(num)
        return start

    def draw_grid(self):
        x = 95.55
        y = 74.4
        for each in self.board:
            if x == 95.55 and y == 74.4:
                for num in each:
                    indx = self.get_indx(x, y)
                    x_indx, y_indx = indx
                    if num != '' and not isinstance(self.board_2[y_indx][x_indx], str):
                        rect = self.canvas.create_rectangle(20 + (x_indx * self.x_size), 40 + y_indx * self.y_size, 20 + (x_indx * self.x_size) + self.x_size,40 + (y_indx * self.y_size) + self.y_size, fill = "#A9A9A9")
                        self.canvas.tag_lower(rect)
                        self.text_place(x, y, num)
                        x += 151.11
                    else:
                        self.text_place(x, y, num)
                        x += 151.11
            else: 
                y += 68.88
                x = 95.55
                for num in each:
                    indx = self.get_indx(x, y)
                    x_indx, y_indx = indx
                    if num != '' and not isinstance(self.board_2[y_indx][x_indx], str):
                        rect = self.canvas.create_rectangle(20 + (x_indx * self.x_size), 40 + y_indx * self.y_size, 20 + (x_indx * self.x_size) + self.x_size,40 + (y_indx * self.y_size) + self.y_size, fill = "#A9A9A9")
                        self.canvas.tag_lower(rect)
                        self.text_place(x, y, num) 
                        x += 151.11
                    else:
                        self.text_place(x, y, num)
                        x += 151.11
                
    def delete_text(self):
        self.canvas.destroy()

    def drawButton(self, main):
        play = Button(main, text = 'reset', command = self.reset)
        play.place(x=20, y = 10, height = 20, width = 35)
    
    def text_place(self, x, y, num):
        self.text = self.canvas.create_text(x, y, text = num, tags = "delete")

sudoku = Sudoku(root)
root.bind("<Button 1>", sudoku.motion) 
root.bind("<Key>", sudoku.key)
root.mainloop()



