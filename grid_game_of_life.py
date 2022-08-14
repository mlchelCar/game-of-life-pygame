import pygame


class GameOfLife():
    def __init__(self, grid_size, height, screen, grid_color=(0, 0, 0), cell_color=(255, 255, 255), verbose=False):
        self.grid_size = grid_size
        self.height = height
        self.cell_size = height*1000/grid_size
        self.screen = screen

        self.grid_color = grid_color
        self.cell_color = cell_color

        self.out = verbose

        self.cells = []
        self.live = []

        for i in range(grid_size):
            line = {}
            pos_count = -1
            for j in range(grid_size):
                pos = (j*self.cell_size/1000, i*self.cell_size/1000)
                pos_count += 1
                line[pos_count] = pos
            self.cells.append(line)
        if self.out:
            print("Grid initialized!")

    def draw_cells(self):
        for line_num, line in enumerate(self.cells):
            for cel in line:
                # if cel % 2 == 0:
                #     self.grid_color = (255, 0, 0)
                # else:
                #     self.grid_color = (0, 0, 255)
                pygame.draw.rect(
                    self.screen, self.grid_color, (self.cells[line_num][cel], (self.cell_size, self.cell_size)))
        pygame.display.update()
        if self.out:
            print("Grid done!")

    def pos_to_cell(self, pos):
        """Given a pygame position, return the corresponding cell"""
        for line_num, line in enumerate(self.cells):
            for cel in line:
                for i in range(int(self.cells[line_num][cel][0]), int(self.cells[line_num][cel][0]+self.cell_size/1000)):
                    for j in range(int(self.cells[line_num][cel][1]), int(self.cells[line_num][cel][1]+self.cell_size/1000)):
                        if (i, j) == pos:
                            return cel, line_num

    def neighbor_cell(self, cell, line):
        """Given a cell position, return the neighbor cells"""
        line0 = line
        line1 = line - 1
        line2 = line + 1
        cell0 = cell - 1
        cell1 = cell + 1
        return [(cell0, line0), (cell1, line0), (cell0, line1), (cell, line1),
                (cell1, line1), (cell0, line2), (cell, line2), (cell1, line2)]

    def add_cell(self, cell, line):
        """Given a cell position, draw the cell"""
        if (cell, line) in self.live:
            return
        self.live.append((cell, line))
        pygame.draw.rect(
            self.screen, self.cell_color, (self.cells[line][cell], (self.cell_size/940, self.cell_size/940)))
        if self.out:
            print('Cell added!')

    def remove_cell(self, cell, line):
        """Given a cell position, draw the original color"""
        if (cell, line) not in self.live:
            return
        self.live.remove((cell, line))
        pygame.draw.rect(
            self.screen, self.grid_color, (self.cells[line][cell], (self.cell_size/940, self.cell_size/940)))
        if self.out:
            print('Cell removed!')

    def tick(self):
        rem_cells = []
        add_cells = []
        if len(self.live) == 0:
            return

        for liv in self.live:
            neighbor = self.neighbor_cell(liv[0], liv[1])
            num = 0
            for cell in neighbor:
                if cell in self.live:
                    num += 1
            if num < 2 or num > 3:
                rem_cells.append(liv)

        for line_num, line in enumerate(self.cells):
            for cell in line:
                if (cell, line_num) in self.live:
                    continue
                neighbor = self.neighbor_cell(cell, line_num)
                num = 0
                for cel in neighbor:
                    if cel in self.live:
                        num += 1
                if num == 3:
                    add_cells.append((cell, line_num))

        for dell in rem_cells:
            self.remove_cell(dell[0], dell[1])

        for add in add_cells:
            self.add_cell(add[0], add[1])
        if self.out:
            print('Tick!')
