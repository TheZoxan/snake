import pygame
from control import Control
from snake import Snake
from gui import Gui

pygame.init()

# Create display game
window = pygame.display.set_mode((441, 441))
pygame.display.set_caption("Snake")
control = Control()
snake = Snake()
gui = Gui()
speed = 0


# Cycle so that the window does not close
while control.flag_game:
    control.control()
    # Create a way out of the game
    window.fill(pygame.Color("black"))
    snake.draw_snake(window)
    gui.draw_level(window)
    if speed % 100 == 0 and control.flag_pause:
        snake.move(control)
        snake.check_end_window()
        snake.animation()
    speed += 2
    pygame.display.flip()
