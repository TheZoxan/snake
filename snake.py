import pygame
from gui import Gui
from control import Control

class Snake:
    def __init__(self):
        self.head = [45, 45]
        self.body = [[45, 45], [34, 45], [23, 45]]
    def move(self, control):
        if control.flag_direction == "RIGHT":
            self.head[0] += 11
        elif control.flag_direction == "LEFT":
            self.head[0] -= 11
        elif control.flag_direction == "UP":
            self.head[1] -= 11
        elif control.flag_direction == "DOWN":
            self.head[1] += 11
    def animation(self):
        self.body.insert(0, list(self.head))
        self.body.pop()

    def draw_snake(self, window):
        for segment in self.body:
            pygame.draw.rect(window, pygame.Color("GREEN"), pygame.Rect(segment[0], segment[1], 10, 10))

    def check_end_window(self):
        if self.head[0] == 419:
            self.head[0] = 23
        elif self.head[0] == 12:
            self.head[0] = 419
        elif self.head[1] == 23:
            self.head[1] = 419
        elif self.head[1] == 419:
            self.head[1] = 34


