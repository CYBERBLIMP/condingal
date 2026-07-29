import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

snake = [(100, 100)]
dx, dy = CELL, 0

food = (
    random.randrange(0, WIDTH, CELL),
    random.randrange(0, HEIGHT, CELL),
)

font = pygame.font.SysFont(None, 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dy == 0:
        dx, dy = 0, -CELL
    if keys[pygame.K_DOWN] and dy == 0:
        dx, dy = 0, CELL
    if keys[pygame.K_LEFT] and dx == 0:
        dx, dy = -CELL, 0
    if keys[pygame.K_RIGHT] and dx == 0:
        dx, dy = CELL, 0

    head = (snake[0][0] + dx, snake[0][1] + dy)

    if (
        head in snake
        or head[0] < 0
        or head[0] >= WIDTH
        or head[1] < 0
        or head[1] >= HEIGHT
    ):
        break

    snake.insert(0, head)

    if head == food:
        food = (
            random.randrange(0, WIDTH, CELL),
            random.randrange(0, HEIGHT, CELL),
        )
    else:
        snake.pop()

    screen.fill(BLACK)

    pygame.draw.rect(screen, RED, (*food, CELL, CELL))

    for part in snake:
        pygame.draw.rect(screen, GREEN, (*part, CELL, CELL))

    score = font.render(f"Score: {len(snake)-1}", True, (255,255,255))
    screen.blit(score, (10,10))

    pygame.display.flip()
    clock.tick(10)

print("Game Over! Score:", len(snake)-1)
pygame.quit()