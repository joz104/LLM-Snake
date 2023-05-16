import pygame
# Initialize Pygame
pygame.init()
# Set up screen and game window
screen = pygame.display.set_mode((600, 480))
font = pygame.font.SysFont("Arial", 30)
# Define snake block size (in pixels)
BLOCKSIZE = 10
# Define the speed of the snake in blocks per second
SPEED = 20
# Set up game variables
pos_x = 350 # x position of the snake head
pos_y = 480 - BLOCKSIZE * 2 // 2 # y position of the snake tail end
speed = SPEED
direction = 'RIGHT' # direction in which the snake is moving (up, down, left or right)
# Set up food variables
food_pos_x = round(random.randrange(0, 600))
food_pos_y = round(random.randrange(480 - BLOCKSIZE * 2, 480))
food_on = False # whether the food is on or off (off by default)
# Set up game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        direction = 'LEFT'
    elif keys[pygame.K_RIGHT]:
        direction = 'RIGHT'
    else:
        direction = '' # no movement (stop)

    if direction == 'UP':
        pos_y -= BLOCKSIZE // 2
    elif direction == 'DOWN':
        pos_y += BLOCKSIZE // 2
    elif direction == 'LEFT':
        pos_x -= BLOCKSIZE // 2
    else: # right
        if food_on:
            food_pos_x = round(random.randrange(0, 600))
            food_pos_y = round(random.randrange(480 - BLOCKSIZE * 2, 480))
        else: # turn off the food if not on
            food_on = False

    if pos_x < food_pos_x and direction == 'RIGHT':
        pos_x += SPEED // 2
    elif pos_y > food_pos_y and direction == 'DOWN':
        pos_y -= BLOCKSIZE // 2

    # draw snake block on the screen
    for i in range(len(snake)):
        pygame.draw.rect(screen, (0, 255, 0), [pos_x + i * SPEED, pos_y - BLOCKSIZE // 2, BLOCKSIZE, BLOCKSIZE])

    # draw food block on the screen
    if food_on:
        pygame.draw.rect(screen, (255, 0, 0), [food_pos_x, food_pos_y - BLOCKSIZE // 2, BLOCKSIZE, BLOCKSIZE])

    # update snake block position on the screen
    if pos_x < food_pos_x and direction == 'RIGHT':
        pos_x += SPEED // 2
    elif pos_y > food_pos_y and direction == 'DOWN':
        pos_y -= BLOCKSIZE // 2

    # check if snake collided with wall or itself (if moving up)
    if pos_x < 0:
        direction = 'LEFT'
    elif pos_x > 599:
        direction = 'RIGHT'
    else:
        direction = '' # no movement (stop)

    if pos_y < 0 or pos_y >= 480 - BLOCKSIZE * 2:
        direction = 'LEFT'
    elif direction == 'DOWN':
        pos_y += SPEED // 2

# quit Pygame window
pygame.quit()