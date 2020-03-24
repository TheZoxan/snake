import pygame
from control import Control
from snake import Snake
pygame.init()

# Create display game
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")
control = Control()
snake = Snake()
speed = 0
# Cycle so that the window does not close
while control.flag_game:
    control.control()
    # Create a way out of the game
    window.fill(pygame.Color("black"))
    snake.draw_snake(window)
    if speed % 100 == 0:
        snake.move(control)
    speed += 2
    pygame.display.flip()   
