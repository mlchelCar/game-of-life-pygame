import tkinter

import pygame

import grid_game_of_life


def main():
    HEIGHT = tkinter.Tk().winfo_screenheight() - 70  # 768
    SCREEN = pygame.display.set_mode((HEIGHT, HEIGHT))
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    GRID_SIZE = 50

    game_grid = grid_game_of_life.GameOfLife(
        GRID_SIZE, HEIGHT, SCREEN, verbose=False)
    FPS = 10
    clock = pygame.time.Clock()

    pygame.init()
    pygame.display.set_caption("Game of Life")
    game_grid.draw_cells()

    run_game = False
    running = True

    while running:
        for ev in pygame.event.get():  # get an itarable object with all the events
            if ev.type == pygame.QUIT:
                running = False
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    print("Quiting!")
                    quit()
                if ev.key == pygame.K_SPACE:
                    print('Run!')
                    game_grid.tick()
                if ev.key == pygame.K_DELETE:
                    run_game = not run_game
                    print(f'Run Game: {run_game}!')
                if ev.key == pygame.K_c:
                    print("Clear!")
                    remov = [c for c in game_grid.live]
                    for cell in remov:
                        game_grid.remove_cell(cell[0], cell[1])

        while True:
            pygame.event.get()

            mouse_pressed = pygame.mouse.get_pressed()
            cell, line = game_grid.pos_to_cell(pygame.mouse.get_pos())
            if mouse_pressed[0]:
                game_grid.add_cell(cell, line)
            elif mouse_pressed[2]:
                game_grid.remove_cell(cell, line)
            else:
                break
            pygame.display.update()

        if run_game:
            game_grid.tick()
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
