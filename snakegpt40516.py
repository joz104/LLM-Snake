import pygame
import time
import random

# Window size
WIDTH = 600
HEIGHT = 400

# Colors (R, G, B)
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Initial snake and food position
snake_pos = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, WIDTH//10)*10, random.randrange(1, HEIGHT//10)*10]
food_spawn = True

# Setting direction variables
direction = 'RIGHT'
change_to = direction

# Initial score
score = 0

# Pygame initialization
pygame.init()
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((WIDTH, HEIGHT))

# FPS (frames per second) controller
fps = pygame.time.Clock()

def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WIDTH//2, HEIGHT//4)
    game_window.fill(BLACK)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, RED, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (WIDTH//10, 15)
    else:
        score_rect.midtop = (WIDTH//2, HEIGHT//1.25)
    game_window.blit(score_surface, score_rect)

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'

    # Direction validation
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Update snake position
    if direction == 'UP':
        snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] - 10])
    if direction == 'DOWN':
        snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] + 10])
    if direction == 'LEFT':
        snake_pos.insert(0, [snake_pos[0][0] - 10, snake_pos[0][1]])
    if direction == 'RIGHT':
        snake_pos.insert(0, [snake_pos[0][0] + 10, snake_pos[0][1]])

    # Game over when snake is outside the screen
    if snake_pos[0][0] >= WIDTH or snake_pos[0][0] < 0 or snake_pos[0][1] >= HEIGHT or snake_pos[0][1] < 0:
        game_over()

    # Game over when snake runs over itself
    for pos in snake_pos[1:]:
        if pos == snake_pos[0]:
            game_over()

    # Spawning food
    if not food_spawn:
        food_pos = [random.randrange(1, WIDTH//10)*10, random.randrange(1, HEIGHT//10)*10]
    food_spawn = snake_pos[0] != food_pos

    # Eating food
    if snake_pos[0] == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_pos.pop()

    # Graphics
    game_window.fill(BLACK)
    for pos in snake_pos:
        pygame.draw.rect(game_window, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, WHITE, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    if snake_pos[0][0] >= WIDTH or snake_pos[0][0] < 0 or snake_pos[0][1] >= HEIGHT or snake_pos[0][1] < 0:
        game_over()
    for pos in snake_pos[1:]:
        if pos == snake_pos[0]:
            game_over()

    show_score(1, WHITE, 'consolas', 20)
    pygame.display.update()
    fps.tick(24)

