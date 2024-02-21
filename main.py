import pygame
import time
from random import randint
from copy import deepcopy

size = (700, 700)
FPS = 25
width = height = 20
n = size[1] // width

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()


def create_grid():
    return [[randint(0, 1) for _ in range(n)] for _ in range(n)]


def check_cell(current_status, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_status[j][i] == 1:
                count += 1

    if current_status[y][x] == 1:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0


def start_game(results):
    current_status = create_grid()
    next_status = [[0 for _ in range(n)] for _ in range(n)]
    count = 1
    cycle = []

    start_time = time.time()

    running = True
    while running:
        screen.fill(pygame.Color('black'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        for i in range(n):
            pygame.draw.line(screen, pygame.Color('white'), (0, (i + 1) * width), (700, (i + 1) * width))
            pygame.draw.line(screen, pygame.Color('white'), ((i + 1) * height, 0), ((i + 1) * width, 700))

        for x in range(1, n - 1):
            for y in range(1, n - 1):
                if current_status[y][x] == 1:
                    pygame.draw.rect(screen, pygame.Color('pink'), (x * height + 2, y * height + 2, height - 2, height - 2))
                next_status[y][x] = check_cell(current_status, x, y)

        current_status = deepcopy(next_status)

        if (count % 2) == 0:
            if current_status == cycle:
                print("GAME OVER")
                print(count)
                running = False

        if (count % 2) == 0:
            cycle = current_status
        count += 1

        pygame.display.flip()
        clock.tick(FPS)

    end_time = time.time()
    total_time = end_time - start_time
    results.append(total_time)


def show_results(results):
    screen.fill(pygame.Color('black'))
    font = pygame.font.Font(None, 36)
    title_text = font.render("Table of Results", True, pygame.Color('white'))
    screen.blit(title_text, (250, 50))

    row_height = 50
    x_start = 100
    y_start = 150

    for i, result in enumerate(results):
        num_text = font.render(str(i + 1), True, pygame.Color('white'))
        time_text = font.render("{:.2f} seconds".format(result), True, pygame.Color('white'))
        screen.blit(num_text, (x_start, y_start + i * row_height))
        screen.blit(time_text, (x_start + 100, y_start + i * row_height))

    back_text = font.render("Back", True, pygame.Color('black'))
    pygame.draw.rect(screen, pygame.Color('white'), (300, 600, 100, 50))
    screen.blit(back_text, (330, 615))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 300 <= mouse_pos[0] <= 400 and 600 <= mouse_pos[1] <= 650:
                    waiting = False


def main():
    results = []
    running = True
    while running:
        screen.fill(pygame.Color('black'))
        font = pygame.font.Font(None, 36)
        title_text = font.render("Game of Life", True, pygame.Color('white'))
        start_text = font.render("Start", True, pygame.Color('black'))
        results_text = font.render("Results", True, pygame.Color('black'))
        exit_text = font.render("Exit", True, pygame.Color('black'))
        screen.blit(title_text, (280, 200))
        pygame.draw.rect(screen, pygame.Color('white'), (300, 300, 100, 50))
        screen.blit(start_text, (320, 315))
        pygame.draw.rect(screen, pygame.Color('white'), (300, 400, 100, 50))
        screen.blit(results_text, (305, 415))
        pygame.draw.rect(screen, pygame.Color('white'), (300, 500, 100, 50))
        screen.blit(exit_text, (330, 515))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 300 <= mouse_pos[0] <= 400:
                    if 300 <= mouse_pos[1] <= 350:
                        start_game(results)  
                    elif 400 <= mouse_pos[1] <= 450:
                        show_results(results)  
                    elif 500 <= mouse_pos[1] <= 550:
                        running = False


if __name__ == "__main__":
    main()
