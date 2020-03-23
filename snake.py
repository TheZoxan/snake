import pygame
pygame.init()

# Create display game
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")
flag_game = True

head = [45, 45]

speed = 0
# Cycle so that the window does not close
while flag_game:
    # Create a way out of the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag_game = False
    window.fill(pygame.Color("black"))
    pygame.draw.rect(window, pygame.Color("green"), pygame.Rect(head[0], head[1], 10, 10))
    if speed % 100 == 0:
        head[0] += 10
    speed += 1
    pygame.display.flip()

