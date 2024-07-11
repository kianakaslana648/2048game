import random

class Game2048:
    def __init__(self):
        self.grid = [[0] * 4 for _ in range(4)]
        self.next_grid = [[0] * 4 for _ in range(4)]
        self.add_new_tile()
        self.add_new_tile()

    def add_new_tile(self):
        empty_cells = [(r, c) for r in range(4) for c in range(4) if self.grid[r][c] == 0]
        if empty_cells:
            r, c = random.choice(empty_cells)
            self.grid[r][c] = 2

    def slide(self, row):
        new_row = [i for i in row if i != 0]
        new_row += [0] * (len(row) - len(new_row))
        return new_row

    def combine(self, row):
        for i in range(len(row) - 1):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] *= 2
                row[i + 1] = 0
        return row

    def move_left(self):
        moved = False
        for r in range(4):
            self.next_grid[r] = self.slide(self.combine(self.slide(self.grid[r])))
        if self.next_grid != self.grid:
            moved = True
        # for r in range(4):
        #     self.grid[r] = self.slide(self.combine(self.slide(self.grid[r])))
        self.grid = self.next_grid
        if moved:
            self.add_new_tile()
            self.add_new_tile()

    def move_right(self):
        moved = False
        for r in range(4):
            self.next_grid[r] = self.slide(self.combine(self.slide(self.grid[r][::-1])))[::-1]
        if self.next_grid != self.grid:
            moved = True
        self.grid = self.next_grid
        if moved:
            self.add_new_tile()
            self.add_new_tile()

    def move_up(self):
        self.grid = self.transpose(self.grid)
        self.next_grid = self.transpose(self.next_grid)
        self.move_left()
        self.grid = self.transpose(self.grid)
        self.next_grid = self.transpose(self.next_grid)

    def move_down(self):
        self.grid = self.transpose(self.grid)
        self.next_grid = self.transpose(self.next_grid)
        self.move_right()
        self.grid = self.transpose(self.grid)
        self.next_grid = self.transpose(self.next_grid)

    def transpose(self, grid):
        return [list(row) for row in zip(*grid)]

    def can_move(self):
        for r in range(4):
            for c in range(4):
                if self.grid[r][c] == 0:
                    return True
                if c < 3 and self.grid[r][c] == self.grid[r][c + 1]:
                    return True
                if r < 3 and self.grid[r][c] == self.grid[r + 1][c]:
                    return True
        return False

    def print_grid(self):
        for row in self.grid:
            print(row)

    def has_won(self):
        for row in self.grid:
            if 2048 in row:
                return True
        return False
