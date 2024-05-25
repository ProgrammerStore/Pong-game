import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong Game')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Paddle and ball dimensions
paddle_width = 15
paddle_height = 100
ball_size = 20

# Paddle positions
player_y = (height - paddle_height) // 2
opponent_y = (height - paddle_height) // 2

# Ball position and velocity
ball_x = width // 2
ball_y = height // 2
ball_velocity_x = random.choice([-7, 7])
ball_velocity_y = random.choice([-7, 7])

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        player_y += 5
    if keys[pygame.K_UP]:
        player_y -= 5

    # Ball movement
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # Ball collision with walls
    if ball_y <= 0 or ball_y >= height - ball_size:
        ball_velocity_y = -ball_velocity_y

    # Ball collision with paddles
    if ball_x <= paddle_width and player_y <= ball_y <= player_y + paddle_height:
        ball_velocity_x = -ball_velocity_x
    if ball_x >= width - paddle_width - ball_size and opponent_y <= ball_y <= opponent_y + paddle_height:
        ball_velocity_x = -ball_velocity_x

    # Update opponent paddle position
    if opponent_y + paddle_height // 2 < ball_y:
        opponent_y += 3
    else:
        opponent_y -= 3

    # Clear the screen
    screen.fill(black)

    # Draw paddles and ball
    pygame.draw.rect(screen, white, pygame.Rect(0, player_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, pygame.Rect(width - paddle_width, opponent_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, white, pygame.Rect(ball_x, ball_y, ball_size, ball_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit the Pygame environment
pygame.quit()
