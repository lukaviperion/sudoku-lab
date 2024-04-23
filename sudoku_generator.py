import random


class SudokuGenerator:
    def __init__(self, row_length=9, removed_cells=40):
        self.row_length = row_length
        self.board = [[0]*self.row_length for _ in range(self.row_length)]
        self.removed_cells = removed_cells
        self.fill_values()

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(row)

    def valid_in_row(self, row, num):
        for r in row:
            if r == num:
                return False
        return True

    def valid_in_col(self, col, num):
        for c in col:
            if c == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if self.get_board()[i][j] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row, col, num):
            return True
        else:
            return False

    def fill_box(self, row_start, col_start):
        rand = 0
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                rand = random.randint(1, 9)
                if self.is_valid(i, j, rand):
                    self.get_board()[i][j] = rand

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(1, 1)
        self.fill_box(2, 2)


    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
