import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
WINDOW_TITLE = "Snake Game"
WINDOW_COLOR = (255, 255, 255)
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 30
BLOCK_SIZE = 10

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

# Set up the font
font = pygame.font.SysFont(None, FONT_SIZE)

# Set up the clock
clock = pygame.time.Clock()

# Set up the game variables
snake_x = WINDOW_WIDTH // 2
snake_y = WINDOW_HEIGHT // 2
snake_dx = BLOCK_SIZE
snake_dy = 0
snake_length = 1
snake_blocks = [(snake_x, snake_y)]
food_x = random.randint(BLOCK_SIZE, WINDOW_WIDTH - BLOCK_SIZE)
food_y = random.randint(BLOCK_SIZE, WINDOW_HEIGHT - BLOCK_SIZE)

# Set up the game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -BLOCK_SIZE
            elif event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = BLOCK_SIZE
            elif event.key == pygame.K_LEFT:
                snake_dx = -BLOCK_SIZE
                snake_dy = 0
            elif event.key == pygame.K_RIGHT:
                snake_dx = BLOCK_SIZE
                snake_dy = 0

    # Move the snake
    snake_x += snake_dx
    snake_y += snake_dy

    # Check if the snake hit the wall
    if snake_x < 0 or snake_x >= WINDOW_WIDTH or snake_y < 0 or snake_y >= WINDOW_HEIGHT:
        game_over = True

    # Check if the snake hit itself
    for block in snake_blocks[1:]:
        if snake_x == block[0] and snake_y == block[1]:
            game_over = True

    # Check if the snake ate the food
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randint(BLOCK_SIZE, WINDOW_WIDTH - BLOCK_SIZE)
        food_y = random.randint(BLOCK_SIZE, WINDOW_HEIGHT - BLOCK_SIZE)
        snake_length += 1

    # Add the new block to the snake
    snake_blocks.append((snake_x, snake_y))
    if len(snake_blocks) > snake_length:
        snake_blocks.pop(0)

    # Draw the window
    window.fill(WINDOW_COLOR)
    pygame.draw.rect(window, (255, 0, 0), (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))
    for block in snake_blocks:
        pygame.draw.rect(window, (0, 255, 0), (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))
    score_text = font.render(f"Score: {snake_length - 1}", True, FONT_COLOR)
    window.blit(score_text, (10, 10))
    pygame.display.update()

    # Set the game speed
    clock.tick(10)

# Quit Pygame
pygame.quit()
