import time
import pygame
import numpy as np

COLOR_BG = (10, 10, 10,)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (170, 170, 170)
COLOR_ALIVE_NEXT = (255, 255, 255)

pygame.init()
pygame.display.set_caption("conway's game of life")


def update(screen, cells, size, lonely, overpop, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row - 1:row + 2, col - 1:col + 2]) - cells[row, col]
        if cells[row, col] == 0:
            color = COLOR_BG
        else:
            color = COLOR_ALIVE_NEXT

        if cells[row, col] == 1:
            if alive < lonely or alive > overpop:  # 1 then 5 - 2 then 3
                if with_progress:
                    color = COLOR_DIE_NEXT
            elif lonely <= alive <= overpop:  # 1 then 5 - 2 then 3
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT

        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return updated_cells


def game(lonely, overpop):
    pygame.init()
    screen = pygame.display.set_mode((1800, 1000))

    cells = np.zeros((100, 180))
    screen.fill(COLOR_GRID)
    update(screen, cells, 10, lonely, overpop)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for Q in pygame.event.get():
            if Q.type == pygame.QUIT:
                pygame.quit()
                return
            elif Q.type == pygame.KEYDOWN:
                if Q.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10, lonely, overpop)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10, lonely, overpop)
                pygame.display.update()

        screen.fill(COLOR_GRID)

        if running:
            cells = update(screen, cells, 10, lonely, overpop, with_progress=True)
            pygame.display.update()

        time.sleep(0.001)


def main():
    lonely = int(input("what loneliness number would you like? "))
    overpop = int(input("what overpopulation number would you like? "))
    game(lonely, overpop)


if __name__ == "__main__":
    main()

 #1 lonely and anything but 2 for overpop is very cool - especially 3