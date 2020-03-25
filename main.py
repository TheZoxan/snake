import pygame
from control import Control
from snake import Snake
from gui import Gui
from food import Food

pygame.init()

# Create display game
window = pygame.display.set_mode((441, 441))
pygame.display.set_caption("Snake")
control = Control()
snake = Snake()
gui = Gui()
food = Food()
gui.init_field()
food.get_food_position(gui)
speed = 0


# Cycle so that the window does not close
while control.flag_game:
    gui.check_win_or_lose()
    control.control()
    # Create a way out of the game
    window.fill(pygame.Color("black"))
    if gui.game == "GAME":
        snake.draw_snake(window)
        food.draw_food(window)
    elif gui.game == "WIN":
        gui.draw_win(window)
    elif gui.game == "LOSE":
        gui.draw_lose(window)
    gui.draw_indicator(window)
    gui.draw_level(window)
    if speed % 100 == 0 and control.flag_pause and gui.game == "GAME":
        snake.move(control)
        snake.check_barrier(gui)
        snake.eat_food(food, gui)
        snake.check_end_window()
        snake.animation()
    speed += 2
    pygame.display.flip()
