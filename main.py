import random


class Board:
    def __init__(self, layout:list=[4,4]):
        self.layout = layout
        self.board = [[0] * layout[0] for _ in range(layout[1])] # what is with the shallow copy and deep copy wtf [[0]*4]*4 will not work beacuse it will just use the same lis 4 time rip
        self.empty_tiles = self.board
        self.last_move = "" # left right up down: this will be used to know which direction to merge

    def print_board(self):
        for row in self.board:
            print(row)
        print(self.board)
        
    
    def get_empty_tiles(self):
        empty_tiles = []
        row_index = 0
        while row_index < len(self.board):
            col_index = 0
            while col_index < len(self.board[row_index]):
                if self.board[row_index][col_index] == 0:
                    empty_tiles.append([row_index, col_index])
                col_index +=1
            row_index+=1
        # print(empty_tiles)
        self.empty_tiles = empty_tiles
    
    def insert_tile(self):
        self.get_empty_tiles()
        tile_choice = random.choice(self.empty_tiles)
        print(tile_choice)
        x = tile_choice[0]
        y = tile_choice[1]
        
        print(x,y)
        prob_of_two = 8
        prob_of_four = 2
        self.board[x][y] = random.choice([2]*prob_of_two + [4]*prob_of_four)
        

    def compress(self, direction):
        new_board = []
        match direction:
            case "right":
                
                for row in self.board:
                    non_zeros = [val for val in row if val != 0]
                    new_board.append([0] * (len(row) - len(non_zeros)) + non_zeros)
                self.board = new_board
                self.last_move = "right"
            case "left":
                for row in self.board:
                    non_zeros = [val for val in row if val != 0]
                    new_board.append(non_zeros + [0] * (len(row) - len(non_zeros)))
                self.board = new_board
                self.last_move = "left"
                
            case "up": # to move up, the numbers should move left after transpose
                self.transpose_board()
                for row in self.board:
                    non_zeros = [val for val in row if val != 0]
                    new_board.append(non_zeros + [0] * (len(row) - len(non_zeros)))
                self.board = new_board 
                self.last_move = "up"
                    
                self.transpose_board() # i don't like this but I'm too lazy to change it back
            case "down": # to move down the numbers should movel right after transpose
                self.transpose_board()
                for row in self.board:
                    non_zeros = [val for val in row if val != 0]
                    new_board.append([0] * (len(row) - len(non_zeros)) + non_zeros)
                    
                    
                self.board = new_board 
                self.last_move = "down"
                self.transpose_board() # i don't like this but I'm too lazy to change it back 
           
            
            
            case _:
                pass
            
                
    
    def transpose_board(self):
        
        transposed_board = list(zip(*self.board))
        transposed_board = [list(x) for x in transposed_board]
        # print("transposed board")
        # for row in transposed_board:
        #     print(row)
        self.board = transposed_board

    def merge(self):
        if self.last_move in ["left", "right"]:
            row_index = 0
            while row_index < len(self.board):
                col_index = 0
                while col_index < len(self.board[row_index])-1:
                    if self.board[row_index][col_index] == 0:
                        pass
                    if self.board[row_index][col_index] != self.board[row_index][col_index + 1]:
                        col_index+=1
                        continue
                    else:
                        self.board[row_index][col_index] = self.board[row_index][col_index] * 2
                        self.board[row_index][col_index + 1] = 0
                        col_index +=2
                row_index +=1
        elif self.last_move in ["up", "down"]:
            row_index = 0
            self.transpose_board()
            while row_index < len(self.board):
                col_index = 0
                while col_index < len(self.board[row_index])-1:
                    if self.board[row_index][col_index] == 0:
                        pass
                    if self.board[row_index][col_index] != self.board[row_index][col_index + 1]:
                        col_index+=1
                        continue
                    else:
                        self.board[row_index][col_index] = self.board[row_index][col_index] * 2
                        self.board[row_index][col_index + 1] = 0
                        col_index +=2
                row_index +=1
            self.transpose_board()
        self.compress(self.last_move)
                    
    
board = Board()
print("2048 Type 'up', 'down', 'left', 'right' to pick the directiion you want to go")

for i in range(100):
    # dir = input("direction: ")
    if i % 4 == 0:
        dir = "up"
    elif i % 3 == 0:
        dir = "right"
    elif i % 2 == 0:
        dir = "down"
    else:
        dir = "left"
    print(i)
    # board.print_board()
    board.compress(dir)
    board.merge()
    
    board.insert_tile()
    print(dir, "completed")
    print(board.last_move)
    board.print_board()
    