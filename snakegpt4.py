import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake settings
snake_size = 20
snake_speed = 15
snake = [[100, 100], [90, 100], [80, 100]]

# Food settings
food_size = 20
food = [random.randrange(1, (WIDTH//food_size)) * food_size, random.randrange(1, (HEIGHT//food_size)) * food_size]

# Movement
direction = 'RIGHT'
clock = pygame.time.Clock()

def game_over():
    font = pygame.font.SysFont('Arial', 40)
    text = font.render('Game Over', True, RED)
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    if direction == 'UP':
        snake.insert(0, [snake[0][0], snake[0][1] - snake_size])
    if direction == 'DOWN':
        snake.insert(0, [snake[0][0], snake[0][1] + snake_size])
    if direction == 'LEFT':
        snake.insert(0, [snake[0][0] - snake_size, snake[0][1]])
    if direction == 'RIGHT':
        snake.insert(0, [snake[0][0] + snake_size, snake[0][1]])

    # Check snake collision with itself
    if snake[0] in snake[1:]:
        game_over()

    # Check snake collision with screen boundaries
    if snake[0][0] < 0 or snake[0][0] >= WIDTH or snake[0][1] < 0 or snake[0][1] >= HEIGHT:
        game_over()

    # Check if snake has eaten food
    if snake[0] == food:
        food = [random.randrange(1, (WIDTH//food_size)) * food_size, random.randrange(1, (HEIGHT//food_size)) * food_size]
    else:
        snake.pop()

    screen.fill(BLACK)

    # Draw snake
    for s in snake:
        pygame.draw.rect(screen, GREEN, (s[0], s[1], snake_size, snake_size))

    # Draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], food_size, food_size))

    pygame.display.flip()

    # Control the game speed
    clock.tick(snake_speed)


