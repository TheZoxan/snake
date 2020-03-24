import pygame


class Snake:
    def __init__(self):
        self.head = [45, 45]

    def move(self, control):
        if control.flag_direction == "RIGHT":
            self.head[0] += 10
        elif control.flag_direction == "LEFT":
            self.head[0] -= 10
        elif control.flag_direction == "UP":
            self.head[1] -= 10
        elif control.flag_direction == "DOWN":
            self.head[1] += 10

    def draw_snake(self, window):
        pygame.draw.rect(window, pygame.Color("GREEN"), pygame.Rect(self.head[0], self.head[1], 10, 10))
